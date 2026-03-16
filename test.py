import requests

webhook_url = "https://discord.com/api/webhooks/1482915114397991037/S9cYhH6W9I8rMELNw0gEnW32MsA1mQlsghuFAT75CYZTamG4ekK4hTZAWfMhV4D1dGzj"

data = {
    "content": "🟢 RETIRO APROBADO\n"
               "👤 Usuario: williambarbona511Dota\n"
               "💰 Monto: $8000\n"
               "🏦 Titular: William Jose Manuel Barbona\n"
               "🔢 CBU/CVU: 4530000800018781747269\n"
               "📱 Cel: 3734526716"
}

requests.post(webhook_url, json=data)