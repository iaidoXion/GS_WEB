import django
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from web.forms import UserForm
from web.commonFun import MenuList
from web.dashboardFun import DashboardDataList
import urllib3
import json
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
ProjectType = SETTING['PROJECT']['TYPE']
Customer = SETTING['PROJECT']['CUSTOMER']
WorldUse = SETTING['PROJECT']['MAP']['World']
KoreaUse = SETTING['PROJECT']['MAP']['Korea']
AreaUse = SETTING['PROJECT']['MAP']['Area']
ZoneUse = SETTING['PROJECT']['MAP']['Zone']


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
menuSettingList = MenuList()

def index(request):
    return render(request, 'common/login.html')

def signup(request):
    """ 계정생성 """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='/')
def dashboard(request):
    chartData = DashboardDataList()
    MapUse = {"WorldUse" : WorldUse, "KoreaUse" : KoreaUse, "AreaUse" : AreaUse, "ZoneUse" : ZoneUse}
    returnData = { 'menuList': menuSettingList, 'chartData' : chartData, 'MapUse' : MapUse, 'Customer' : Customer}
    #print(chartData)
    return render(request, 'tanium/dashboard.html', returnData)

@login_required(login_url='/')
def assetWeb(request):
    returnData = { 'menuList': menuSettingList }
    return render(request, 'tanium/asset.html', returnData)

@login_required(login_url='/')
def software(request):
    return render(request, 'tanium/software.html', menuSettingList)

@login_required(login_url='/')
def security(request):
    returnData = {'menuList': menuSettingList}
    return render(request, 'tanium/security.html', returnData)

@login_required(login_url='/')
def report(request):
    returnData = { 'menuList': menuSettingList }
    return render(request, 'tanium/report.html', returnData)

@login_required(login_url='/')
def setting(request):
    returnData = {'menuList': menuSettingList}
    return render(request, 'common/setting.html', returnData)

@login_required(login_url='/')
def userinfo(request):
    returnData = {'menuList': menuSettingList}
    return render(request, 'common/change_password.html', returnData)

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {'form': form, 'menuList': menuSettingList})

# @login_required(login_url='/login/')
# def logout(request):
#     if request.session['user'] : #로그인 중이라면
#         del(request.session['user'])
#
#     return redirect('/') #홈으로
def csrf_failure(request, reason=""):
    messages.success(request, '잘못된 접근입니다.')
    return render(request, 'common/login.html')

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)

# def lockout(request, credentials, *args, **kwargs):
#     messages.success(request, '로그인 실패 횟수가 5회를 초과하여 10분간 로그인이 제한됩니다.')
#     return redirect('login')

def lock_out(request):
    return render(request, 'lockout.html')
