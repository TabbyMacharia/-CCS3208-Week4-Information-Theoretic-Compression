# CCS 3208 – Week 4: Information-Theoretic Compression

## Overview

This repository contains my practical laboratory work for **CCS 3208 – Multimedia Systems**, focusing on information-theoretic compression techniques.

The laboratory explores how different lossless compression algorithms represent data efficiently by examining symbol probabilities, repeated patterns, and coding strategies.

## Learning Objectives

- Calculate symbol probabilities, self-information, and Shannon entropy.
- Implement Huffman coding and evaluate its coding efficiency.
- Explore arithmetic coding through interval encoding and decoding.
- Implement Lempel–Ziv–Welch (LZW) compression and decompression.
- Compare theoretical compression limits with practical compression results.

## Laboratory Tasks

### Task 1: Probability, Self-Information and Entropy
- Calculate symbol frequencies and probabilities.
- Determine the self-information of individual symbols.
- Compute Shannon entropy.
- Compare entropy with fixed-length encoding.

### Task 2: Huffman Coding
- Construct a Huffman coding tree.
- Generate prefix-free binary codes.
- Encode and decode messages.
- Calculate average code length.
- Evaluate coding efficiency and codebook overhead.

### Task 3: Arithmetic Coding
- Explore cumulative probability intervals.
- Perform interval encoding and decoding.
- Trace interval narrowing for different messages.
- Examine the limitations of floating-point arithmetic in practical implementations.

### Task 4: LZW Compression
- Trace dictionary construction manually.
- Implement LZW encoding and decoding.
- Compare repetitive and less repetitive input sequences.
- Explore the application of LZW in GIF image compression.

## Technologies and Tools

- **Programming Language:** Python 3.14.7
- **IDE:** PyCharm
- **Operating System:** Windows 11
- **Version Control:** Git and GitHub
- **Libraries:** Python Standard Library

## Project Structure

```text
CCS3208-Week4-Information-Theoretic-Compression/
│
├── task1_pythonverification.py
├── task2_huffmanencoderanddecoder.py
├── task3_intervalencoderanddecoder.py
├── task4_LZWencoderanddecoder.py
├── README.md
└── .gitignore
```

## Running the Programs

1. Clone the repository:

   ```bash
   git clone https://github.com/TabbyMacharia/-CCS3208-Week4-Information-Theoretic-Compression.git
   ```

2. Open the project in PyCharm.

3. Ensure Python 3.9 or later is installed.

4. Run the individual Python scripts:

   ```bash
   python task1_pythonverification.py
   python task2_huffmanencoderanddecoder.py
   python task3_intervalencoderanddecoder.py
   python task4_LZWencoderanddecoder.py 
   ```

The programs use Python's standard library and do not require additional third-party packages.

## Key Concepts Explored

- Shannon Entropy
- Self-Information
- Variable-Length Coding
- Huffman Coding
- Arithmetic Coding
- Dictionary-Based Compression
- Lempel–Ziv–Welch (LZW)
- Lossless Compression
- Compression Efficiency

## Conclusion

This practical laboratory provided hands-on experience with fundamental information-theoretic compression techniques. Through manual calculations and Python implementations, I explored how different algorithms reduce data representation while preserving the original information.

The exercises also demonstrated the relationship between theoretical entropy, coding efficiency, dictionary construction, and practical compression overhead.

---

**Course:** CCS 3208 – Multimedia Systems  
**Practical:** Week 4 – Information-Theoretic Compression  
**Author:** Tabitha Macharia
