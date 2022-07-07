%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Presentation parameters for the RadApt_grating experiments:
% - RADAPT_baselineRB.py
% - RADAPT_gratings.py
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Parameters of the OLED SCREEN
d               = 60                                   % eye-screen distance in cm
dd              = 2.*d;                                % 2*d
pixelPitch      = 0.315;                               % pixel size in mm (0.315 for the Alienware OLED)
ScreenWidthpix  = 3840;                                % screen width in pixels 
ScreenHeightpix = 2160;                                % screen height in pixels 
ScreenWidthCm   = pixelPitch*ScreenWidthpix/10;        % screen width in cm  
ScreenHeightCm  = pixelPitch*ScreenHeightpix/10;       % screen height in cm  
alphaW          = 2.*atand(ScreenWidthCm/dd)           % alpha = 2arctan(w/2d) % screen width in degrees
alphaH          = 2.*atand(ScreenHeightCm/dd)          % alpha = 2arctan(w/2d) % screen height in degrees


%%% in SASAKI et al 2006
% eccentricities = 15.5°
% gabor size = 1.2°
% gabor SF = 4 cpd

%%% here:
% Eccentricities tested = 8° + 16°
% gabor size = 2° /  1°
% gabor SF = 4 cpd


% Calculate Gabor position in pixels for ECC = 8°
Eccentricity = 8
w = 2*d*tand(Eccentricity./2) %Exc en cm
wPix = round(w*ScreenWidthpix/ScreenWidthCm)%Exc en pix

% Calculate Gabor position in pixels for ECC = 16°
Eccentricity = 16
w = 2*d*tand(Eccentricity./2) %Exc en cm
wPix = round(w*ScreenWidthpix/ScreenWidthCm)%Exc en pix

% Calculate Gabor position in pixels for ECC = 12°
Eccentricity = 12
w = 2*d*tand(Eccentricity./2) %Exc en cm
wPix = round(w*ScreenWidthpix/ScreenWidthCm)%Exc en pix

% Calculate Gabor position in pixels for ECC = 15°
Eccentricity = 15
w = 2*d*tand(Eccentricity./2) %Exc en cm
wPix = round(w*ScreenWidthpix/ScreenWidthCm)%Exc en pix



% Calculate Gabor size in pixels for Gabor size = 2°
dvaW            = 2;                                 % angular size (width) 
dvaH            = 2;                                 % angular size (height) 
realW           = dd*tand(dvaW./2);                  % gabor width in cm = 2dtan(alpha/2)
realH           = dd*tand(dvaH./2);                  % gabor height in cm = 2dtan(alpha/2)
realWpix        = round(realW*ScreenWidthpix/ScreenWidthCm) % gabor width in pixels
realHpix        = round(realH*ScreenWidthpix/ScreenWidthCm) % gabor height in pixels

% Calculate Gabor size in pixels for Gabor size = 0.7°
dvaW            = 0.7;                                 % angular size (width) 
dvaH            = 0.7;                                 % angular size (height) 
realW           = dd*tand(dvaW./2);                  % gabor width in cm = 2dtan(alpha/2)
realH           = dd*tand(dvaH./2);                  % gabor height in cm = 2dtan(alpha/2)
realWpix        = round(realW*ScreenWidthpix/ScreenWidthCm) % gabor width in pixels
realHpix        = round(realH*ScreenWidthpix/ScreenWidthCm) % gabor height in pixels

% Calculate Gabor size in pixels for Gabor size = 1.25°
dvaW            = 1.25;                                 % angular size (width) 
dvaH            = 1.25;                                 % angular size (height) 
realW           = dd*tand(dvaW./2);                  % gabor width in cm = 2dtan(alpha/2)
realH           = dd*tand(dvaH./2);                  % gabor height in cm = 2dtan(alpha/2)
realWpix        = round(realW*ScreenWidthpix/ScreenWidthCm) % gabor width in pixels
realHpix        = round(realH*ScreenWidthpix/ScreenWidthCm) % gabor height in pixels

% Calculate Gabor size in pixels for Gabor size = 6°
dvaW            = 6;                                 % angular size (width) 
dvaH            = 6;                                 % angular size (height) 
realW           = dd*tand(dvaW./2);                  % gabor width in cm = 2dtan(alpha/2)
realH           = dd*tand(dvaH./2);                  % gabor height in cm = 2dtan(alpha/2)
realWpix        = round(realW*ScreenWidthpix/ScreenWidthCm) % gabor width in pixels
realHpix        = round(realH*ScreenWidthpix/ScreenWidthCm) % gabor height in pixels





% Calculate Gabor spatial frequency in cycles / pixels for Gabor SF = 4 cycles / degrees
dva             = 1;                                 % 1° 
dvaPix          = ScreenWidthpix/screenWidthCm       % How many pixels is 1° 
SFdva           = 4;                                 % cycles per degrees
realSF          = dd*tand(SFdva./2)                  % cycles per cm
realSFpix       = realSF*dva/dvaPix                  % cycles per pix




% Calculate size of the grey gaussian background (and the adapter stimuli). For radius = 30°
dvaRadius       = 30;                                % angular size (radius) 
dvaDiameter     = 2*dvaRadius;                       % angular size (diameter) 
realDiameter    = dd*tand(dvaDiameter./2);          % diameter in cm
realDiameterPix = round(realDiameter*screenWidthPix/screenWidthCm) % diameter in pixels
% Size of the gaussian background and adapters should be realDiameterPix

