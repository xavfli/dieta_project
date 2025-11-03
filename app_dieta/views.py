from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserMessage
import requests

# Telegram konfiguratsiyasi
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHANNEL_OR_CHAT_ID"

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def submit_user(request):
    if request.method == "POST":
        first_name = request.POST.get("name")
        last_name = request.POST.get("surname")
        telegram_user = request.POST.get("telegram")
        message = request.POST.get("message")
        phone = request.POST.get("phone")

        user = UserMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            telegram=telegram_user,
            phone=phone,
            message=message,
        )

        # Telegramga yuborish
        text = f"📩 Yangi foydalanuvchi:\n👤 {first_name} {last_name}\n📞 {phone}\n💬 {message}\n🔗 @{telegram_user}"
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      data={"chat_id": CHAT_ID, "text": text})

        return render(request, "thanks.html")
    return JsonResponse({"error": "Faqat POST so‘rov qabul qilinadi"}, status=400)


def send_to_telegram(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.CHANNEL_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegramga yuborishda xatolik:", e)
