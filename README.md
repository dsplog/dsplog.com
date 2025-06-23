## Codes referred in the blog on SignalProcessing and AI [https://dsplog.com](https://dsplog.com)

This repository organizes code snippets referred to in the articles on the website [https://dsplog.com](https://dsplog.com).

## Code Organization

### [Multiclass classification with Softmax](code/gradients_multiclass_classification/)
Read the detailed article : [Gradients for multiclass classification with Softmax](https://dsplog.com/2025/06/22/gradients-for-multi-class-classification-with-softmax/)

- [derivative of softmax](derivative_softmax.ipynb) - implementation of softmax gradient calculation
- [gradients for cross entropy loss](gradients_cross_entropy_loss.ipynb) - computing gradients for cross entropy loss function
- [training multi-class classification](training_multiclass_classification.ipynb) - complete training pipeline for multi-class classification
- [label smoothing implementation](training_label_smoothing.ipynb) - label smoothing technique for improving classification

### [BPSK Bit Error Rate](code/bpsk_bit_error_rate/)

Read the detailed article: [Bit Error Rate (BER) for BPSK modulation
](https://dsplog.com/2007/08/05/bit-error-probability-for-bpsk-modulation/)

- `bit_error_rate_vs_snr.ipynb`: Analysis of BER vs SNR for BPSK
- `bpsk_unequal_source_probabilities.ipynb`: BPSK with non-uniform source probabilities
- `bpsk_with_noise.ipynb`: BPSK modulation with AWGN noise

### [Gradients in Binary Classification](code/gradients_binary_classification/)

Read the detailed article: [Gradients for Binary Classification](https://dsplog.com/2025/05/17/gradients-for-binary-classification/)

- `gradients_binary_cross_entropy_loss.ipynb`: Computing gradients for binary cross entropy
- `sigmoid_and_derivative.ipynb`: Sigmoid function and its derivative
- `training_loop_binary_classification.ipynb`: Complete training loop implementation
- `training_probit.ipynb`: Training with probit regression

### [Gradients for Linear Regression](code/linear_regression/)

Read the detailed article: [Gradients for Linear Regression](https://dsplog.com/2025/05/01/gradients-for-linear-regression/)


- `gradients_absolute_function.ipynb`: Gradients for absolute error function
- `gradients_analytic_vs_finite_difference_vs_pytorch.ipynb`: Comparison of gradient computation methods
- `linear_regression.ipynb`: Basic linear regression implementation
- `linear_regression_mean_abs_error.ipynb`: Linear regression with MAE loss
- `linear_regression_pytorch.ipynb`: PyTorch implementation of linear regression

Feel free to explore the notebooks and use the code as a reference for your projects!
