#!/bin/bash

echo "🎯 Ping atılacak adresi girin:"
read -r adres

if [ -z "$adres" ]; then
    echo "❌ Hata: Adres boş olamaz!"
    exit 1
fi

echo "📡 '$adres' adresine ping atılıyor..."
ping -c 4 "$adres"

if [ $? -ne 0 ]; then
    echo "⚠️ Ping başarısız oldu. Adresi kontrol et."
else
    echo "✅ Ping başarılı!"
fi
