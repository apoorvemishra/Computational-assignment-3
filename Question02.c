#include <stdio.h>
#include <math.h>
#include <fftw3.h>

#define N 1024 // Number of samples

int main() {
    int i;
    double x[N], y[N];
    fftw_complex *in, *out;
    fftw_plan plan;
    FILE *file;

    // Create sinc function
    for (i = 0; i < N; i++) {
        x[i] = (i - N / 2) != 0 ? sin((i - N / 2)) / ((i - N / 2)) : 1.0;
        y[i] = 0.0;
    }

    // Allocate memory for FFT
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    // Create FFT plan
    plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    // Copy data to FFT input array
    for (i = 0; i < N; i++) {
        in[i][0] = x[i];
        in[i][1] = y[i];
    }

    // Perform FFT
    fftw_execute(plan);

    // Open file for writing
    file = fopen("fft_result.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write FFT result to file
    fprintf(file, "# Frequency Amplitude\n");
    for (i = 0; i < N; i++) {
        fprintf(file, "%d %f\n", i - N / 2, sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]));
    }

    // Close file
    if (fclose(file) != 0) {
        printf("Error closing file!\n");
        return 1;
    }

    printf("File 'fft_result.txt' successfully created.\n");

    // Free memory and destroy plan
    fftw_destroy_plan(plan);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
