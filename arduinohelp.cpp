#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <thread>
#include <vector>
#include <SerialStream.h>

using namespace std;
using namespace LibSerial;

int main() {
    // Open serial port
    SerialStream serial("/dev/ttyACM0", ios_base::in);

    // Set baud rate
    serial.SetBaudRate(BaudRate::BAUD_9600);

    // Open output file
    string filename = "data.csv";
    ofstream output(filename);

    // Record data for 10 seconds
    chrono::seconds duration(10);
    chrono::steady_clock::time_point start_time = chrono::steady_clock::now();
    vector<int> data;
    while (chrono::steady_clock::now() - start_time < duration) {
        string line;
        getline(serial, line);
        int value = stoi(line);
        data.push_back(value);
    }

    // Write data to output file
    for (int i = 0; i < data.size(); i++) {
        output << data[i] << endl;
    }

    // Close output file and serial port
    output.close();
    serial.Close();

    return 0;
}
