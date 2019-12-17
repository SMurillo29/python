%% Condiciones iniciales
clc,            close all,          clear all
a = -2;         b = 2;          limite=2e-1;        conFib = 1;
conIte = 1
x = -3:0.5:3;
funcion = @(x )x.^3 - 3*x + 2;

NumFib = (b - a)/limite;

fibonacci = [0 1];
while NumFib >= fibonacci(end)
    fibonacci(conFib + 2) = fibonacci(conFib + 1) + fibonacci(conFib);
    conFib = conFib +1;
end


lamda = a + (fibonacci(end - 2) / fibonacci(end))*(b - a);
miu = a + (fibonacci(end - 1) / fibonacci(end))*(b - a);
fLamda = funcion(lamda);
fMiu = funcion(miu);
%% Calculos de miu y lamda
while size(fibonacci, 2) > 2

    if fLamda>fMiu
        a = lamda;
        lamda = miu;
        fLamda = fMiu;
        miu = a + (fibonacci(end - 1) / fibonacci(end))*(b - a);
        fMiu = funcion(miu);
    elseif fLamda<fMiu
        b = miu;
        miu = lamda;
        fMiu = fLamda;
        lamda = a + (fibonacci(end - 2) / fibonacci(end))*(b - a);
        fLamda = funcion(lamda);
    end
    fibonacci(end) = [];
    plot(lamda,fLamda,'rd', miu, fMiu, 'bo')
    hold on
end
plot(x, funcion(x), 'k')
