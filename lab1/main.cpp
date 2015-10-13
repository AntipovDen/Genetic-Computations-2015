#include <iostream>
#include <random>
#include <assert.h>
#include <vector>

using namespace std;


const double ALPHA = 0.5;
const double CROSS = 0.8;
random_device rd_d;
mt19937 gen_d(rd_d());
random_device rd_i;
mt19937 gen_i(rd_i());
uniform_real_distribution<> rand_double(0, 1);

double f(vector<double> &x)
{
    for (double xi : x)
    {
        cout << xi << ' ';
    }
    cout << '\n';
    string res;
    cin >> res;
    if (res == "Bingo") exit(0);
    return atof(res.c_str());
}

double beta[5] = {1.0, 2.0, 3.0, 4.0, 5.0};
double gammas[5] = {2.0, 1.8, 1.6, 1.4, 1.2};
double* alpha[5];
//
//double best = 9000;

double tf(vector<double> &x)
{
    for (double xi : x)
    {
        assert(xi >= -10.0 && xi <= 10.0);
    }
    double min = 9000.0;
    for (int i = 0; i < 5; i++)
    {
        double res = 0.0;
        for (int j = 0; j < x.size(); j++)
        {
            res += (x.at(j) - alpha[i][j]) * (x.at(j) - alpha[i][j]);
        }
        res *= gammas[i];
        res += beta[i];
        if (res < min) min = res;
    }
    if (min < 2.01)
    {
        cout << "Bingo!\n" << min;
        exit(0);
    }
    return min + rand_double(gen_d) - 0.5;
}

 
int main()
{
    int n;
    cin >> n;


    for (int i = 0; i < 5; i++)
    {
        alpha[i] = new double[n];
        for (int j = 0; j < n; j++)
        {
            alpha[i][j] = rand_double(gen_d) * 20.0 - 10.0;
        }
    }


    int pop_size = 100 * n;

    uniform_int_distribution<> rand_individual(0, (pop_size - 1) * (pop_size - 2) - 1);


    vector<vector<double>> pop(pop_size);
    vector<vector<double>> next_pop(pop_size);
    vector<double> values(pop_size);
    vector<double> next_values(pop_size);

    for (int i = 0; i < pop_size; i++)
    {
        for (int j = 0; j < n; j++)
        {
            pop.at(i).push_back(rand_double(gen_d) * 20.0 - 10.0);
            next_pop.at(i).push_back(0.0);
        }
        values.at(i) = f(pop.at(i));
    }

    while(true)
    {
        for (int i = 0; i < pop_size; i++)
        {
            int r = rand_individual(gen_i);

            int b = r % (pop_size - 1);
            r /= (pop_size - 1);
            int c = r % (pop_size - 2);
            if (b >= i) b++;
            if (c >= min(i, b)) c++;
            if (c >= max(i, b)) c++;

            // new individual with crossover
            for (int j = 0; j < n; j++)
            {
                if (rand_double(gen_d) < CROSS)
                {
                    next_pop.at(i).at(j) = pop.at(i).at(j) + ALPHA * (pop.at(b).at(j) - pop.at(c).at(j));
                    if (next_pop.at(i).at(j) > 10.0) next_pop.at(i).at(j) = 10.0;
                    else if (next_pop.at(i).at(j) < -10.0) next_pop.at(i).at(j) = -10.0;
                }
                else
                {
                    next_pop.at(i).at(j) = pop.at(i).at(j);
                }
            }

            //check candidate
            double next_value = f(next_pop.at(i));
            if (next_value <= values.at(i))
            {
                next_values.at(i) = next_value;
            }
            else {
                for (int j = 0; j < n; j++) {
                    next_pop.at(i).at(j) = pop.at(i).at(j);
                }
                next_values.at(i) = values.at(i);
            }
        }
        swap(next_pop, pop);
        swap(next_values, values);
    }
}
