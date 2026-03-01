# -*- coding: utf-8 -*-
import urllib.request
import os
import zipfile

def download_dejavu_fonts():
    """Download DejaVu fonts which have excellent Cyrillic support"""
    
    # DejaVu fonts official download
    url = "https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.zip"
    
    target_dir = r"D:\OneDrive\Рабочие файлы\Рабочий стол\Экзокортекс\PACK-cattle-science\process\working\fonts"
    os.makedirs(target_dir, exist_ok=True)
    
    zip_path = os.path.join(target_dir, "dejavu.zip")
    
    print("Downloading DejaVu fonts...")
    try:
        urllib.request.urlretrieve(url, zip_path)
        print(f"Downloaded to {zip_path}")
        
        # Extract
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        
        # Find the TTF files
        ttf_dir = os.path.join(target_dir, "dejavu-fonts-ttf-2.37", "ttf")
        if os.path.exists(ttf_dir):
            fonts = [f for f in os.listdir(ttf_dir) if f.endswith('.ttf')]
            print(f"\nAvailable fonts: {', '.join(fonts[:10])}...")
            
            # Copy main fonts to target dir
            for font in ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf', 'DejaVuSerif.ttf']:
                src = os.path.join(ttf_dir, font)
                dst = os.path.join(target_dir, font)
                if os.path.exists(src):
                    import shutil
                    shutil.copy(src, dst)
                    print(f"Copied: {font}")
        
        # Clean up zip
        os.remove(zip_path)
        import shutil
        shutil.rmtree(os.path.join(target_dir, "dejavu-fonts-ttf-2.37"), ignore_errors=True)
        
        print(f"\nFonts ready in: {target_dir}")
        return target_dir
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    download_dejavu_fonts()
