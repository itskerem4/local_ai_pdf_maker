# Local Ai Pdf Maker
# Yerleşik Yapay Zeka Modeli İle Pdf Oluşturma


```markdown
# Ollama Model Response to PDF

This Python script interacts with a locally installed LLaMA model through the Ollama CLI, generates a response based on a user-provided prompt, and saves the output to a PDF file. The script supports Unicode characters and uses the DejaVuSans font for compatibility with Turkish and other special characters.

---

## Features

- **User Input for Model and Prompt**: 
  - Allows the user to specify the LLaMA model and the prompt at runtime.
- **PDF Output**:
  - Generates a PDF file containing the model's response.
- **Unicode Support**:
  - Ensures proper rendering of Turkish characters using the DejaVuSans font.

---

## Prerequisites

### 1. Install Ollama CLI
Ensure that the Ollama CLI is installed and properly configured on your system. You can download it from [Ollama's official website](https://ollama.ai/).

### 2. Install Python Dependencies
The script requires the following Python libraries:
- `subprocess` (built-in)
- `fpdf`

Install `fpdf` with pip if not already installed:
```bash
pip install fpdf
```

### 3. Download the DejaVuSans Font
Place the `DejaVuSans.ttf` font file in the same directory as the Python script.

You can download the font from the official [DejaVu Fonts GitHub](https://github.com/prawnpdf/prawn/blob/master/data/fonts/DejaVuSans.ttf).

---

## Usage

1. **Run the Script**:
   ```bash
   python ollama_to_pdf.py
   ```

2. **Enter Inputs**:
   - **Model Name**: Enter the name of the LLaMA model (e.g., `llama3.2:3b`).
   - **Prompt**: Enter the prompt you'd like to send to the model.
   - **File Name**: Specify the name for the PDF file (without `.pdf`).

3. **Output**:
   The generated PDF will be saved in the same directory as the script.

---

## Example

### Input:
```
Please Enter Exact Model Name: llama3.2:3b
Please enter the prompt you want to send to your Model: What is the capital of Turkey?
Please Specify File Name: capital
```

### Output:
- A PDF file named `capital.pdf` containing the model's response:
```
Ankara.
```

---

## Troubleshooting

1. **Ollama Not Found**:
   Ensure the Ollama CLI is installed and accessible via the terminal. Add it to your system's PATH if needed.

2. **UnicodeDecodeError**:
   Ensure the prompt and response support UTF-8 encoding. Python's `subprocess` should use `encoding="utf-8"` as specified in the script.

3. **Missing Font Error**:
   Verify that `DejaVuSans.ttf` is in the same directory as the script.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Author

Created by **Kerem Kaplan**.

For questions or contributions, feel free to open an issue or submit a pull request.

---

# Ollama Model Yanıtını PDF'e Kaydetme

Bu Python betiği, Ollama CLI üzerinden yerel olarak kurulu LLaMA modeline bağlanarak kullanıcının verdiği bir prompta yanıt üretir ve bu yanıtı PDF dosyasına kaydeder. Betik, Unicode karakter desteği sağlar ve Türkçe uyumluluğu için DejaVuSans fontunu kullanır.

---

## Özellikler

- **Model ve Prompt İçin Kullanıcı Girişi**:
  - Model adı ve promptu çalıştırma sırasında belirtebilirsiniz.
- **PDF Çıktısı**:
  - Model yanıtını içeren bir PDF dosyası oluşturur.
- **Unicode Desteği**:
  - Türkçe karakterler için uyumlu çıktı sağlar.

---

## Gereksinimler

### 1. Ollama CLI Kurulumu
Ollama CLI'nın sisteminize kurulu ve doğru şekilde yapılandırıldığından emin olun. CLI'yı [Ollama'nın resmi web sitesi](https://ollama.ai/) üzerinden indirebilirsiniz.

### 2. Python Kütüphaneleri
Betik, aşağıdaki Python kütüphanelerine ihtiyaç duyar:
- `subprocess` (Python ile gelir)
- `fpdf`

`fpdf` kütüphanesini yüklemek için:
```bash
pip install fpdf
```

### 3. DejaVuSans Fontunu İndirme
`DejaVuSans.ttf` dosyasını Python betiği ile aynı klasöre koyun.

Font dosyasını [DejaVu Fonts GitHub]([https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf](https://github.com/prawnpdf/prawn/blob/master/data/fonts/DejaVuSans.ttf)) bağlantısından indirebilirsiniz.

---

## Kullanım

1. **Betik Çalıştırma**:
   ```bash
   python ollama_to_pdf.py
   ```

2. **Girdi Girin**:
   - **Model Adı**: LLaMA modelinin tam adını girin (ör. `llama3.2:3b`).
   - **Prompt**: Modelinize göndermek istediğiniz promptu yazın.
   - **Dosya Adı**: Oluşturulacak PDF dosyası için bir ad belirtin (uzantısız).

3. **Çıktı**:
   Oluşturulan PDF dosyası, betiğin bulunduğu dizine kaydedilecektir.

---

## Örnek

### Girdi:
```
Please Enter Exact Model Name: llama3.2:3b
Please enter the prompt you want to send to your Model: Türkiye'nin başkenti neresidir?
Please Specify File Name: baskent
```

### Çıktı:
- Oluşturulan `baskent.pdf` dosyası şu yanıtı içerir:
```
Ankara.
```

---

## Sorun Giderme

1. **Ollama Bulunamadı**:
   Ollama CLI'nın kurulu olduğundan ve terminalden erişilebilir olduğundan emin olun. Gerekirse CLI'yı sistem PATH'ine ekleyin.

2. **UnicodeDecodeError**:
   UTF-8 kodlamasına uygun giriş ve çıkış kullanıldığından emin olun. Python'daki `subprocess`, `encoding="utf-8"` kullanmalıdır.

3. **Font Eksik Hatası**:
   `DejaVuSans.ttf` dosyasının betikle aynı dizinde bulunduğunu kontrol edin.

---

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

---

## Yazar

Bu proje **Kerem Kaplan** tarafından oluşturulmuştur.

Sorularınız veya katkılarınız için lütfen bir sorun oluşturun veya pull request gönderin.
```
