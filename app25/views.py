import random
import time
import qrcode
from django.shortcuts import render, redirect
from django.contrib import messages

from app25.models import OTPModel


def showIndex(request):

    return render(request,'index.html')


def loginDetails(request):
    uname = request.POST.get('t1')
    pwd = request.POST.get('t2')
    if uname == 'amara' and pwd == 'Ramu27':
        no = random.randint(100000,999999)
        OTPModel(otp=no).save()
        qr = qrcode.make("Your OTP Is : "+str(no))
        qr.save(r"app25/static/images/ramu.jpg")
        return render(request,'qrcode.html')
    else:
        messages.error(request,'Invalid Input.')
        return redirect('main')



def otpVerify(request):
    otp = request.POST.get('otp')
    if otp == str(no):
        return redirect('main')
    else:
        messages.error(request,'Invalid OTP.')
        return redirect('main')