# AI Based Behavior-Adaptive Steganography – Secure Image Messaging

## Overview
AI Based Behavior-Adaptive Steganography is a secure image-based data hiding system that embeds encrypted messages inside images using adaptive pixel selection techniques. The system dynamically adjusts embedding behavior based on image characteristics to reduce detectability and improve resistance against steganalysis methods.

---

## Features

- Encrypted message embedding inside images  
- Adaptive pixel selection based on image behavior  
- Support for high-resolution (4K) images  
- Password-based secure encoding and decoding  
- Reduced statistical anomalies for better security  
- Fast encoding and decoding pipeline  
- Web-based interface for ease of use  

---

## Tech Stack

- Backend: Python, Flask  
- Frontend: HTML, CSS, JavaScript  
- Image Processing: Pillow (PIL), NumPy  
- Security: Symmetric encryption with password-derived key system  

---

## How It Works

1. User uploads an image  
2. Input message is encrypted using a password-based key  
3. Image is analyzed for pixel distribution and structural behavior  
4. Encrypted data is embedded into selected adaptive pixel locations  
5. Output image remains visually unchanged  
6. Receiver extracts and decrypts the message using the same password  

---

## Modules

### Encoder
- Encrypts the input message  
- Embeds encrypted bits into image pixels  

### Decoder
- Extracts hidden data from image  
- Decrypts message using password  

### Adaptive Engine
- Analyzes image characteristics  
- Selects optimal embedding positions  

---

## Security Highlights

- Large key space based on encryption method (~2^128)  
- Password-dependent decoding mechanism  
- Resistant to basic steganalysis techniques  
- Reduced detectability through adaptive embedding strategy  

---


