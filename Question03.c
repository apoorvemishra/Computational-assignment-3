#include <stdio.h>
#include <math.h>
#include <gsl/gsl_fft_complex.h>

#define N 1024 // Number of samples
#define PI 3.14159265358979323846

int main() {
    int i;
    double x[N], y[N];

    // Create sinc function
    for (i = 0; i < N; i++) {
        x[i] = (i - N / 2) != 0 ? sin((i - N / 2) * PI) / ((i - N / 2) * PI) : 1.0;
        y[i] = 0.0;
    }

    // Perform Fourier transform
    gsl_fft_complex_radix2_forward(x, 1, N);

    // Open file for writing
    FILE *file = fopen("fft_result.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write FFT result to file
    fprintf(file, "Frequency\tAmplitude\n");
    for (i = 0; i < N; i++) {
        fprintf(file, "%d\t\t%f\n", i - N / 2, sqrt(x[i] * x[i] + y[i] * y[i]));
    }

    // Close file
    fclose(file);

    return 0;
}
