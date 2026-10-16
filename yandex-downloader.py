import requests
import os
import time

def download_yandex_public_folder(public_key, target_folder="YandexDownloads"):
    # Базовый URL API Яндекса для работы с публичными ссылками
    base_url = "https://cloud-api.yandex.net/v1/disk/public/resources"
    
    def fetch_items(path=""):
        params = {"public_key": public_key, "limit": 1000}
        if path:
            params["path"] = path
        
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"[ОШИБКА] Код {response.status_code} для пути '{path}'.")
            if response.status_code == 429:
                print("Сработал антифрод Яндекса (Too Many Requests). Нужно увеличить паузу.")
            return []
        
        return response.json().get("_embedded", {}).get("items", [])

    def download_file(url, save_path):
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    # Запись чанками предотвращает переполнение оперативной памяти
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"  [+] Успешно скачан: {os.path.basename(save_path)}")
        except Exception as e:
            print(f"  [-] Ошибка при скачивании {os.path.basename(save_path)}: {e}")

    def process_directory(current_path, local_dir):
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
            
        items = fetch_items(current_path)
        for item in items:
            if item["type"] == "dir":
                print(f"\n[Папка] {item['name']}")
                process_directory(item["path"], os.path.join(local_dir, item["name"]))
            elif item["type"] == "file":
                print(f"[*] Получение ссылки для файла: {item['name']}...")
                # Для каждого файла запрашиваем прямую ссылку на скачивание
                dl_url_req = requests.get(f"{base_url}/download", params={"public_key": public_key, "path": item["path"]})
                
                if dl_url_req.status_code == 200:
                    download_url = dl_url_req.json().get("href")
                    download_file(download_url, os.path.join(local_dir, item["name"]))
                    
                    # Искусственная задержка для обхода блокировок Яндекса
                    time.sleep(1.5) 
                else:
                    print(f"  [-] Не удалось получить ссылку. Код: {dl_url_req.status_code}")

    print("Начинаем анализ структуры диска...")
    process_directory("", target_folder)
    print("\nПроцесс завершен.")

# === Запуск скрипта ===
if __name__ == "__main__":
    # Вставьте вашу ссылку на Яндекс Диск сюда:
    YANDEX_LINK = "https://disk.yandex.ru/d/7gi3IcRf-x6A9w" 
    
    download_yandex_public_folder(YANDEX_LINK, target_folder="MIPT_Downloads")
