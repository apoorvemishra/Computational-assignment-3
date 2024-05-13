#include <stdio.h>
#include <math.h>
#include <fftw3.h>

#define N 1024 // Number of samples
#define PI 3.14159265358979323846

double gaussian(double x) {
    return exp(-x * x);
}

int main() {
    int i;
    double x[N], y[N];
    fftw_complex *in, *out;
    fftw_plan plan;

    // Create Gaussian function
    for (i = 0; i < N; i++) {
        x[i] = (i - N / 2) * 0.1; // Adjust the scaling factor as needed
        y[i] = 0.0;
    }

    // Allocate memory for FFT
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    // Create FFT plan
    plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // Copy data to FFT input array
    for (i = 0; i < N; i++) {
        in[i][0] = gaussian(x[i]);
        in[i][1] = 0.0;
    }

    // Perform FFT
    fftw_execute(plan);

    // Output FFT result
    printf("Frequency\tAmplitude\n");
    for (i = 0; i < N; i++) {
        printf("%d\t\t%f\n", i - N / 2, sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]));
    }

    // Free memory and destroy plan
    fftw_destroy_plan(plan);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
