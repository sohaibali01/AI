clc
clear all
close all

load fisheriris

PL = meas(1:100,3);
PW = meas(1:100,4);
species = species(1:100);




%% perceptron algo
y=zeros(size(species));
y(1:50)=1;
y(51:100)=-1;

figure;
scatter3(PL,PW,y);
xlabel('PL')
ylabel('PW')
zlabel('Class Labels')
hold on

w=[rand rand];
b=rand;
x=[PL PW];

[m,n] = size(x) ;
idx = randperm(m) ;

for i=1:100
    if y(idx(i))*(w*x(idx(i),:)'+b)<0
        w=w+y(idx(i))*x(idx(i),:);
        b=b+y(idx(i));
    end
end

x1=PL;
x2=PW;
X = [ones(length(x1),1) x1 x2];
x1fit = min(x1):1:max(x1);
x2fit = min(x2):0.1:max(x2);
[X1FIT,X2FIT] = meshgrid(x1fit,x2fit);
YFIT = b + w(2)*X1FIT + w(1)*X2FIT;
mesh(X1FIT,X2FIT,YFIT)

figure;
h1 = gscatter(PL,PW,species,'krb','ov^',[],'off');
h1(1).LineWidth = 2;
h1(2).LineWidth = 2;
legend('Setosa','Versicolor','Location','best')
hold on

f = @(x1,x2) b + w(1)*x1 + w(2)*x2;
h2 = fimplicit(f,[.9 7.1 0 2.5]);
h2.Color = 'r';
h2.LineWidth = 2;
h2.DisplayName = 'Boundary between Versicolor & Setosa';

