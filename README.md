<!--![image of qcchallenge logo](qcc_banner.png) -->
# Welcome to IBM Quantum Challenge!
[日本語はこちら](#ibm-quantum-challengeへようこそ)<br/>
[한글은 여기](#ibm-quantum-challenge환영합니다)<br/>
 

## IMPORTANT : [Final exercise submission rules](#final-exercise-submission-rules)


## Hello, quantum world.

As we approach the end of 2020, we would like to engage the community with new exciting set of challenges, and further push limits of our quantum systems to achieve another yet significant milestone. 

Our first competitive coding contest [IBM Quantum Challenge](https://ibmquantum.angelhack.com/)  was held in November 2019, attracting both seasoned coders and newbies from all over the world to start their journey in Quantum Computing.
In May 2020, we celebrated our fourth anniversary of IBM Quantum Experience with another Challenge where 1,745 people from 45 countries came together to solve four problems making total use of the 18 IBM Quantum systems on the IBM Cloud exceeding 1 billion circuits a day. 

Starting Nov 9th at 9am JST, we present you with three weeks of new challenges that will help grow your knowledge, skills, and understanding of quantum computing and Qiskit to tackle problems using some well-known quantum algorithms.

In recognition of your participation, we are awarding digital badges to those who complete all exercises.

Note that participation is allowed for those who have applied and received official confirmation from the challenge organizers only. 

## Programming Environment
IBM Quantum Challenge will be hosted on IBM Quantum Experience (a.k.a. IQX). IQX allows you to build, execute and evaluate your quantum circuits within a self-contained Jupyter notebook environment without downloading anything to your computer. 

On Nov 9, 2020 when the challenge site opens, participants will see a set of exercises hosted in this self-contained Jupyter notebook environment where you can write and run your code directly from and make submissions of your answers. 

Please note that the challenge site with exercises hosted in this Jupyter notebook environment is only accessible by applicants who confirmed participation upon receiving a confirmation email from the event organizers. 

## Preparation
In many cases, you may prefer to run your code locally when working on the exercises before you make your submission in the IBM Quantum Experience environment. In such case, you will need to install **Qiskit** to your computer. Qiskit is a Python based opensource framework for working with quantum computers at the level of pulses, circuits, and algorithms. Please see the [Qiskit.org](https://qiskit.org) page for more details.

Qiskit can be installed by using *pip*:

```
$ pip install qiskit
```

Please check out [Install Qiskit](https://qiskit.org/documentation/install.html) or [YouTube video](https://www.youtube.com/watch?v=M4EkW4VwhcI) for a step by step installaion guide.

## Challenge Index
The challenge content has been shared with the public on the following dates.<br/>

| Week  | Challenge | Message from Dr. Ryoko |　Available on (JST) |
| ---     | ---    | --- |  --- |
| Week 0 |[For Beginners: The atoms of computation](exercises/week-0/ex_0_en.ipynb) | [Episode 1](https://youtu.be/eLw7fWb2xv4) |Now Live | 
| Week 1 |[Learning Challenge Exercise I-A](https://github.com/qiskit-community/IBMQuantumChallenge2020/blob/iqx/exercises/week-1/ex_1a_en.ipynb) <br/>[Learning Challenge Exercise I-B](https://github.com/qiskit-community/IBMQuantumChallenge2020/blob/iqx/exercises/week-1/ex_1b_en.ipynb)|  [Episode 2](https://youtu.be/f8TEd_51rHI) | Nov 9th 2020 | 
| Week 2  |[Learning Challenge Exercise II-A](https://github.com/qiskit-community/IBMQuantumChallenge2020/blob/main/exercises/week-2/ex_2a_en.ipynb) <br/>[Learning Challenge Exercise II-B](https://github.com/qiskit-community/IBMQuantumChallenge2020/blob/main/exercises/week-2/ex_2b_en.ipynb)| [Episode 3](https://youtu.be/kLizHnvTguE), [Episode 4](https://youtu.be/25PcR5Pn4hk) | Nov 16th 2020 |
| Week 3  |[Final Challenge](https://quantum-computing.ibm.com/jupyter/user/IBMQuantumChallenge2020/week-3/final_en.ipynb) | [Episode 5](https://youtu.be/Bkk5-j6rpoM) | Nov 23rd 2020 |


## Final Exercise Submission Rules
For valid submissions we ask that your solution adheres to the below rule.<br/>
* Please implement the quantum circuit within **28 qubits**.
* Use Grover's algorithm you learned in Week1 & 2 with **iteration ＝ 1**.
* The initial state for Grover's algorithm must be equal probability distributions. For example, if you want use only 3 computational bases for 2 qubits instead of 4 as the initial state. Then, the state will be sqrt(1/3)(|00⟩+|01⟩+|11⟩).
* Please note that you can get the answer with the same endian as the one used in Week2 explanation. You should map the index of the problem into four classical registers c[0:4] in binary. c[0] is the highest bit and c[3] is the lowest bit. For example, when mapping 12, the furthest left bit of 1100 will be mapped to c[0].
* Make sure you **create an oracle** that **doesn't require knowledge of what the answers are**. (For example, you are not allowed to create an oracle by using a classical optimization solver to get your answers for it.)  
With the exception of the Unroller, which is required for decomposing your circuit to calculate quantum costs, you are not allowed to use any existing transpiler passes nor original transpilers for making simplifications in this competition.
* Please **do not run jobs in succession** even if you are concerned that your job is not running properly. This can create a long queue and clog the backend. You can check whether your job is running properly at: https://quantum-computing.ibm.com/results  
* Your score for this exercise will be same as the cost of your QuantumCircuit. The lower the cost, the better.
* Judges will check top 10 solutions manually to see if the solutions adhere to the rules. **Please note that your ranking is subject to change after the challenge period as a result of the judging process**. 
* Top 10 participants will be recognized and asked to submit a write up on how they solved the exercise.
* **When mapping the board information into your quantum circuit, you must not change the board information from the original one. (i.e. Do not rearrange the asteroid positions, nor rotate, invert, swap rows and columns.)** 
<br/>
