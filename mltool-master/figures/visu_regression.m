
clear all
close all
addpath(genpath('..'))

%% Loading dataset

dataset='ECOG';
[xapp,yapp,xtest,ytest]=get_dataset(dataset);

%% Dataset visualization

figure(1)

nvisu=200
dvisu=20
subplot(2,1,1)

plot(yapp(1:nvisu))
title('Finger flexion')

subplot(2,1,2)


plot(xapp(1:nvisu,1:dvisu))
ylim([-5,5])
title('Extracted features from ECoG')


%% LDA classifier + visu

lambda=1e2;
[w,w0]=ridge(xapp,yapp,lambda);

ypred_app=xapp*w+w0;


%% plot regression result


figure(1)
set(gcf,'defaulttextinterpreter','latex');

lw=2;
fs=16;

nvisu=200
dvisu=20
subplot(2,1,1)

plot(yapp(1:nvisu))
hold on
plot(ypred_app(1:nvisu),'r')
hold off
title('Flexion du pouce','FontSize',fs)
l=legend('Donn\''ees r\''eelles','Pr\''ediction f(x) Ridge')
set(l,'FontSize',fs,'interpreter','latex')
subplot(2,1,2)


plot(xapp(1:nvisu,1:dvisu))
ylim([-5,5])
title('Caract\''eristiques extraites de signaux ECoG','FontSize',fs)
print('-depsc','visu_reg.eps')

