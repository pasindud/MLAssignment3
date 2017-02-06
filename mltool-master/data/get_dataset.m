function [xapp,yapp,xtest,ytest]=get_dataset(dataset,options)
%  [xapp,yapp,xtest,ytest]=get_dataset(dataset)
% 
% Input:
%  dataset : type of dataset defalt='M1'
%       - 'MI': motor imagery
%           options : subject number (1->9)
%       - 'P300': P300 speller dataset (no option)
%       - 'ECOG': finger flexion prediction from ECOG (no option)
%
% See README file for more details on the datasets


if nargin<2
    options=1;
end

switch dataset
    
    case 'MI'
        load('MI_train')
        load('MI_test')
        
        xapp=featureTrainSet{options};
        yapp=xapp(:,end);
        xapp=xapp(:,1:end-1);
        
        yapp=(yapp==2)-(yapp==1);
    
        xtest=featureTestSet{options};
        ytest=xtest(:,end);
        xtest=xtest(:,1:end-1);    
        
        ytest=(ytest==2)-(ytest==1);
        
        
    case 'ECOG'
        load('ECoG_Finger')

        napp=2000;
        
        xapp=Xall(1:napp,:);
        yapp=Yall(1:napp);
        
        
        xtest=Xall(napp+1:end,:);
        ytest=Yall(napp+1:end);       
     
    case 'P300'
        load('P300_data')

        napp=2000;
        
        xapp=X(1:napp,:);
        yapp=Y(1:napp);
        
        
        xtest=X(napp+1:end,:);
        ytest=Y(napp+1:end);       
             
    
    otherwise 
        error('unknown dataset')
end
