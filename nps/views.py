from operator import itemgetter

from django.shortcuts import render

from nps.models import Stock
from .nps import get_nps_data, get_code, get_real_time, get_past_time
# Create your views here.
from nps.models import Nps


def home(request):
    sum = 0
    all_instance = Nps.objects.all()

    if not all_instance:
        data = get_nps_data()
        name = data['종목명']
        ex_value = data['평가액']
        asset_rate = []
        k = data['자산군 내 비중']
        for i in k:
            asset_rate.append(str(round(i*100,1))+'%')
        share = data['지분율']

        for i in range(len(name)):
            Nps.objects.create(name=name[i], ex_value=ex_value[i], asset_rate=asset_rate[i], share=share[i])

    else:
        stock_instance = Stock.objects.all()
        if not stock_instance:
            data = get_code()
            name_list = list(data.keys())

            for i in name_list:
                try:
                    nps_instance = Nps.objects.filter(name=i)[0]
                    stock_data = data['%s' % i]
                    Stock.objects.create(name=nps_instance, code=stock_data[0], value=stock_data[1])
                except Exception:
                    pass

    all_instance2 = Stock.objects.all()
    for i in all_instance2:
        sum += int(i.name.benefit)
        now_price = get_real_time(i.code)[0]
        stock_number = get_real_time(i.code)[1]
        big_memory = int(now_price*stock_number/100)
        share = float(i.name.share)
        now_price = big_memory * share
        i.name.now = int(now_price)
        i.name.save()
        print(0)

        if i.name.past:
            past_price = get_past_time(i.code)
            past_memory = int(past_price*stock_number/100)

            past = past_memory*share
            i.name.past = int(past)
            i.name.save()
            print(1)

        if i.name.rate:
            print(i.name.past)
            rate = ((int(float(i.name.now))/int(float(i.name.past)))-1)*100
            i.name.rate = round(rate, 2)
            i.name.save()
            print(2)
        if i.name.benefit:
            benefit = int(i.name.now)-int(i.name.past)
            i.name.benefit = benefit
            i.name.save()
            print(3)

    return render(request, 'nps/nps.html', {'data2': all_instance2, "sum": sum})


def home2(request):
    sum_past = 0
    sum = 0
    sum_now = 0
    data = Stock.objects.all()
    for i in data:
        sum += int(i.name.benefit)
        sum_past += int(i.name.past)
        sum_now += int(i.name.now)

    sum_rate = round(((sum_now/sum_past)-1)*100, 4)
    return render(request, 'nps/nps_index.html', {'data2': data, "sum": sum, 'sum_rate': sum_rate})