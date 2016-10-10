function  KFSM_TOF_NO_MO
clear;clear global;clc;
warnstr = warning('off');
delete log;
warning(warnstr);
diary on;
diary('log');
tic;
disp(datestr(now));
disp('Kinetic_fsolve_module is Running now...')
disp('Written By Chen JianFu @ ECUST at 2014/4/4')
format long e;
digits(500);
[Reactions,Rline,Parameters,Pline] = ReadINCAR();
[Matrix,myBasic,mySite] = ExtractCoefficient(Reactions,Rline);
nReaction = length(Reactions);
disp(['Find ' num2str(nReaction) ' Recation Equation(s) : ']);
disp(char(strrep(strrep(Reactions,'+',' + '),'<->',' <-> ')));
disp(['Find ' num2str(length(mySite)) ' Reaction Site(s) : ' strrep(cell2mat(strcat(mySite,',')),',',' ')]);
RPspecies = sum(sum(Matrix(:,:,[end-1 end]),3));
disp(['Reactant Species : ' strrep(cell2mat(strcat(myBasic(RPspecies<0),',')),',',' ')]);
disp(['Production Species : ' strrep(cell2mat(strcat(myBasic(RPspecies>0),',')),',',' ')]); ...
disp(['Intermediate Species : ' strrep(cell2mat(strcat(myBasic(RPspecies(1:end - length(mySite))==0),',')),',',' ')]);
disp(['Find ' num2str(length(myBasic)) ' Reaction Species : ' strrep(cell2mat(strcat(myBasic,',')),',',' ') ]);

disp([char(10) 'Try to Generate Reaction Kinetic Rate Equation now...']);
[fp,fc,fq,fpr,fcr,fqr,r,r0,Qsum] = CreateRateEquations(Matrix,myBasic,mySite);

osym0 = findsym(r);
osym0 = sort(regexp(osym0,',','split'));
Nsyms = length(osym0);

symstr = '';
for i = 1:Nsyms ;
    symstr = [symstr ' ' osym0{i}];
end
eval(['syms ' symstr '  real positive']);
Variables = osym0;
disp([char(10) 'Try to Read Input Parameters in INCAR now...']);
globallist = GetVariables(Parameters,Pline,Variables);
if ~isempty(globallist)
    warnstr = warning('off', 'Control:parameterNotSymmetric');
    eval(['global ' globallist]);
    warning(warnstr);
end

disp('Try to Initialize now...');
[globalvars,yChan,yEqui,yInit,lmax,yp,mysym] = Initialization(osym0,globallist,fpr,fcr,fqr,r0);
disp([char(10) 'The Symbol-Cross-References : '])
disp(mysym.');
if ~isempty(globalvars)
    warning off;
    eval(['global ' globalvars]);
    warning on;
end

yInit = yInit(yChan);
% fqo = fq;
fqt = fqr;
for ix = 1: length(Qsum)
    fq(ix,end - length(Qsum) + ix) = Qsum(ix) - Q0(ix);
    fqt(ix,end - length(Qsum) + ix) = Qsum(ix) - sym(['Q0(' num2str(ix) ')']);
end

disp([char(10) 'Try to Generate Kinetic Rate Steady-State Equation now...']);
F = [fp; fc; fq].';
F = F(yp);
Ft = [fpr; fcr; fqt].';
Ft = Ft(yp);
pEqui = yEqui > 0;
if (sum(pEqui));
    disp([char(10) 'Deal with Reaction ' num2str(sort(yEqui(pEqui))) ' in Equilibrium ']);
    F(pEqui) = r(yEqui(pEqui));
    Fp = find(pEqui);
    for i = 1:length(Fp)
        Ft(Fp(i)) = sym(['r(' num2str(yEqui(Fp(i))) ')']);
    end
end
F = F(yChan);
Ft = Ft(yChan);
s = char(Ft);
s([1:8,end-1:end]) = [];
disp(regexprep(strrep(s,'], [',char(10)),'[[]]',''));
disp([char(10) 'Expand Equations Based On P C Q :']);
s = char(F);
s([1:8,end-1:end]) = [];
disp(regexprep(strrep(s,'], [',char(10)),'[[]]',''));
% Fs = eval(F.');
% disp([char(10) 'Evaluate Equations :']);
% s = char(Fs.');
% s([1:8,end-1:end]) = [];
% disp(regexprep(strrep(s,'], [',char(10)),'[[]]',''));

% Fo = [fp; fc; fqo].';
% Fo = Fo(yp);
% Fo = Fo(yChan);
% Fo = subs(Fo,mysym(2,:),mysym(1,:));
% odestr = char(Fo.');
% odestr([1:8,end-1:end])=[];
% odestr = strrep(odestr,',',';');
% eval(['odefun=@(t,y,kf,kr,RT' strrep(globalvars,' ',',') ')' odestr ])
warnstr = warning('off');
delete odefun.m;
copyfile('myfun.m','odefun.m','f');
delete myfun.m;
warning(warnstr);

k = 0;
osymn = osym0(yChan);
Nsite = length(Qsum);
for ix = 1: Nsite
    tstr = sort(regexp(findsym(Qsum(ix)),',','split')) ;
    nvar(ix) = length(tstr);
    for jx = 1:length(tstr)
        k = k + 1;
        pvar(k) = mystrMatch(osymn,tstr{jx});
        y0(pvar(k)) = Q0(ix);
    end
end
for in = Nsite:-1: 1
    if in == Nsite
        pinit = (1:nvar(in))'+ min(pvar) -1;
        prodN = nvar(in);
    else
        pinit = [reshape(repmat(1:nvar(in),prodN,1),prodN*nvar(in),1) repmat(pinit,nvar(in),1) + nvar(in)];
        prodN = prodN * nvar(in);
    end
end
Y0 = repmat(yInit,prodN,1);
Y0(:,pvar) = 0;
Ya = repmat(y0,prodN,1);
for i = 1:prodN
    Y0(i,pinit(i,:)) = Ya(i,pinit(i,:));
    if prod(double(Y0(i,:) == yInit))
        Y0(i,:) = [];
    end
end

F = subs(F);
r = subs(r);
r0 = subs(r0);
if isempty(npar)
  npar = 1;
end
%% parall set
myCluster = parcluster();
nparm = myCluster.NumWorkers;
npar = min(npar,nparm);
npars = matlabpool('size');
parIsopen =  npars > 0;
if npar ~= 1
    if parIsopen && npar ~= npars
       matlabpool close;
       matlabpool(myCluster,npar);
    elseif ~parIsopen
        matlabpool(myCluster,npar);
    end
end
diary off;
KFSM(1,T,Ex,F,r,r0,yInit,lmax,symstr,Y0);
diary on;
diary('log');
toc;
disp(datestr(now));
disp('Kinetic_fsolve_module is finished now...')
disp('Written By Chen JianFu @ ECUST at 2014/4/4')
diary off;

function KFSM(iR,T,Ex,F,r,r0,yInit,lmax,symstr,Y0)
global keV kBT_h
mypath = pwd;
if exist('result','dir') == 0
    mkdir result; 
end
warnstr = warning('off');
delete(['result/log_' num2str(iR)]);
warning(warnstr);
diary on;
diary(['result/log_' num2str(iR)]);
eval(['syms ' symstr '  real positive']);


% load('Entropy.mat');
% Ss = interp1(Tp,Sp,T,'spline');
% E_TdS = Ss.*repmat(T,1,3)/1000/96.45;

kB = 1.3806505e-23;
NA = 6.0221367e23;
h = 6.62606957e-34;
e = 1.60217653e-19;
keV = e/T/kB;
RT = kB*T*NA;
kBT_h = kB/h*T;
NT = length(Ex);
ytry = yInit;   
for ix = 1:NT
    disp([char(10) 'Run the ' num2str(ix) ' now ...' char(10)]);
    [G0,Ea] = initGE(Ex(ix));
    [kf,kr] = RateConstCalc(Ea,G0);
    Fn = eval(subs(F.'));
    ysym = findsym(Fn);
    [ystr,ysort] = sort(regexp(ysym,',','split'));

    symfuns = char(Fn);
    symfuns = symfuns(10:end - 3);
    disp('Try numeric::fsolve now...');
    [ysol,solveStatus] = tryfsolve(symfuns,yInit,ysym,ytry,kf,kr,RT,Y0);
%    [y1,y2,y3] = solve(Fn);
%     ysol = [y1;y2;y3];
    for i = 1:length(ystr);
        disp([ ystr{i} blanks(lmax + 3 - length(ystr{i})) ' =   ' num2str(double(ysol(i)),'%16.10e')]);
    end
    y(ix,:) = double(ysol);
    ytry = double(ysol);
    dF(ix,:) = double(mysubs(Fn,ystr,ysol)');
    Rneti = double(mysubs(eval(r),ystr,ysol));
    Rnet(ix,:) = Rneti;
    Rfri = double(mysubs(eval(r0),ystr,ysol));
    R(ix,:,:) = [Rfri Rneti];
    Z(ix,:) = Rfri(:,2)./Rfri(:,1);
end
%% calculate TOF
TOF = log10(Rnet(:,3) + Rnet(:,7));
%% plot figure of TOF and save the figure
h1 = figure(1);
% p1 = plot(Ea_d,TOF,'k',Ea_d,TOF1,[MColor{mkind(1)} '--'],Ea_d,TOF2,[MColor{mkind(2)} '--']);
% ylim([ -40 0]);
p = plot(Ex,TOF,'k');
% set(p,'LineWidth',3);
xlabel('E_I^a^d (eV)');
ylabel('log_1_0(TOF)');
% title(['TOF: -T(' num2str(T) ')' ],'fontsize',18,'Color','r');
legend('r')
% set(h1,'Visible','off');
% scrsz = get(0,'ScreenSize');
% set(h1,'Position',scrsz);
% h2 = figure;
% plot(Ex,log10(y(:,1)),'b-.',Ex,log10(y(:,2)),'r-');
% xlabel('E_I^a^d (eV)');
% ylabel('log_1_0(Q)');
% legend('Q_I','Q_*')
% h3 = figure;
% plot(Ex,log10(Z(:,1)),'b-.',Ex,log10(Z(:,2)),'r-')
% xlabel('E_I^a^d (eV)');
% ylabel('log_1_0(Z)');
% legend('Z_1','Z_2');
filen = [ mypath '/TOF_T' num2str(T) ];
save(filen,'TOF','y','dF','Rnet','R','Z');
filen1 = [ mypath '/TOF_T' num2str(T) ];
saveas(h1,[ filen1 '.fig']);
saveas(h1,[ filen1 '.tif']);
% filen2 = [ mypath '/Cov_T' num2str(T) ];
% saveas(h2,[ filen2 '.fig']);
% saveas(h2,[ filen2 '.tif']);
% filen3 = [ mypath '/Rev_T' num2str(T) ];
% saveas(h3,[ filen3 '.fig']);
% saveas(h3,[ filen3 '.tif']);
close(h1);
% close(h2);
% close(h3);
diary off;
function [Reactions,Rline,Parameters,Pline] = ReadINCAR(INCAR)
if nargin == 0
    INCAR = 'INCAR';
end
myPath = pwd;
fid = fopen([ myPath '/' INCAR],'rt');
ix = 0;
jx = 0;
iline = 0;
while fid > 0 && ~feof(fid)
    var = fgets(fid);
    if var == -1
        disp('The INCAR is empty or not existed, please check it and run later !!! ');
        diary off;
        quit;
    end
    iline = iline + 1;
    p = strfind(var,'%');
    var(p:end) = [];
    p = strfind(var,'!');
    var(p:end) = [];
    var = strrep(var,char(10),'');
    var = strrep(var,char(13),'');
    if ~isempty(strrep(var,' ' ,''))
        if ~isempty(strfind(strrep(var,' ',''),'<->'))
            ix = ix + 1;
            Reactions{ix} = var;
            Rline(ix) = iline;
        else
            jx = jx + 1;
            Parameters{jx} = var;
            Pline(jx) = iline;
        end
    end
end
Reactions = strrep(Reactions,' ','');
if fid > 0
    fclose(fid);
else
    fprintf('input file %s : is not existed.\n',INCAR);
    diary off;
    quit;
end

function [Matrix,myBasic,mySite] = ExtractCoefficient(Reactions,Rline)
Sbasic = '#';
mySite = [];
myBasic = [];
temp = char(Reactions)';
temp = temp(:)';
t  = isempty(strfind(temp,[Sbasic '1'])) & strfind(temp,Sbasic);
if sum(t)
    mySite{1} = Sbasic;
end
for ix = 1:length(Reactions)
    a = Reactions{ix};    
    pofArrows(ix) = strfind(a,'<->');
    a = strrep(a,'<->','+');
    alist = regexp(a,'+','split');
    list{ix} = alist;
    Ns = length(mySite);
    for ik = 1:Ns
        alist = strrep(alist,mySite{ik},'');   
    end 
    for il = 1:length(alist)
        alist = strrep(alist,'(p)','');
        alist = strrep(alist,'(c)','');       
        if strfind(alist{il},Sbasic)
            Ns = length(mySite);
            mySite{Ns + 1} = [Sbasic num2str(Ns + 1)];
            alist = strrep(alist,mySite{Ns + 1},'');
        end
        if ~isempty(alist{il}) && ~isvarname(alist{il})
            disp([char(10) 'Find Illegal Variable As Name Of Species : ' alist{il} ' at line ' num2str(Rline(ix))]);
            diary off;
            quit;
        end
    end
    for jx = 1:length(alist)
        if ~isempty(alist{jx})
            strIsfound = mystrMatch(myBasic,alist(jx));
        else
            continue;
        end
        if strIsfound == 0
            myBasic{length(myBasic)+1} = alist{jx};
        end
    end
end
Ns = length(mySite);
myBasic = sort(myBasic);
Matrix =  zeros(length(list),length(myBasic) + Ns,Ns + 2);
for ix = 1:length(list)
    mark = 0;
    for jx = 1:length(list{ix})
        alist = list{ix};
        mark = mark + length(alist{jx}) + 1;
        if (mark <= pofArrows(ix))
            sign = -1;
        else
            sign = 1;
        end
        psite0 = mystrMatch(myBasic,alist(jx)) + mystrMatch(strcat(myBasic,'(p)'),alist(jx));
        if psite0
            Matrix(ix,psite0,end) = Matrix(ix,psite0,end) + sign;
            continue;
        end
        psite1 =  mystrMatch(strcat(myBasic,'(c)'),alist(jx));
        if psite1
            Matrix(ix,psite1,end -1 ) = Matrix(ix,psite1,end - 1) + sign;
            continue;
        end
        for kx = 1:Ns
            psitea = mystrMatch(strcat(myBasic,mySite(kx)),alist(jx));
            if psitea
                Matrix(ix,psitea,kx) = Matrix(ix,psitea,kx) + sign;
                break;
            end
        end
        psites = mystrMatch(mySite,alist(jx));
        if psites
            Matrix(ix,end - Ns + psites,psites) = Matrix(ix,end - Ns + psites,psites) + sign;
        end

    end
end

function [strIsfound] = mystrMatch(mystring,searchstring)
strIsfound = 0;
for ix = 1:length(mystring)
    if strcmp(mystring(ix),searchstring)
        strIsfound = ix;
        break;
    end
end

function [fp,fc,fq,fpr,fcr,fqr,r,r0,Qsum] = CreateRateEquations(Matrix,myBasic,mySite)
pbasic = 'P';
cbasic = 'C';
qbasic = 'Q';
kbasic = 'k';
rbasic = 'r';
% Sbasic = '#';
fpbasic = 'dP';
fcbasic = 'dC';
fqbasic = 'dQ';
tbasic = '/dt';
rFbasic = 'rF';
rRbasic = 'rR';
syms RT
[M,N,Ns] = size(Matrix);
mySite0 = regexprep(mySite,'#[ 1-9]','v');
mySite0 = regexprep(mySite0,'#','v');
myBasic = [myBasic,mySite0];
for ix = 1:N
    order = myBasic{ix};
    P(ix) = sym([pbasic '_' order]);
    FP(ix) = sym([fpbasic '_' order tbasic]);
    C(ix) = sym([cbasic '_' order]);
    FC(ix) = sym([fcbasic '_' order tbasic]);
    for iy = 1:Ns - 2
        if Ns == 3
            iys = '';
        else
            iys = num2str(iy);
        end
        Q(iy,ix) = sym([qbasic iys '_' order]);
        FQ(iy,ix) = sym([fqbasic iys '_' order tbasic]);
    end
end
for ix = 1:M
    ixs = num2str(ix);
    order = ['(' ixs ')'];
    ks(ix,1) = sym([kbasic 'f' order]);
    ks(ix,2) = sym([kbasic 'r' order]); 
    rs(ix,1) = sym([rbasic order ]);
    rFs(ix,1) = sym([rFbasic order ]);
    rRs(ix,1) = sym([rRbasic order ]);
end
pMatrix = Matrix(:,:,Ns);
cMatrix = Matrix(:,:,Ns - 1);
sMatrix = Matrix(:,:,1:Ns - 2);
pfMatrix = pMatrix;
prMatrix = pMatrix;
cfMatrix = cMatrix;
crMatrix = cMatrix;
sfMatrix = sMatrix;
srMatrix = sMatrix;
pf = pMatrix > 0;
pr = pMatrix < 0;
cf = cMatrix > 0;
cr = cMatrix < 0;
sf = sMatrix > 0;
sr = sMatrix < 0;
pfMatrix(pr) = 0;
prMatrix(pf) = 0;
cfMatrix(cr) = 0;
crMatrix(cf) = 0;
sfMatrix(sr) = 0;
srMatrix(sf) = 0;
Pm = ones(M,1)*P;
rF = Pm.^-prMatrix;
rR = Pm.^pfMatrix;
Cm = ones(M,1)*C;
rF = rF.*Cm.^-crMatrix;
rR = rR.*Cm.^cfMatrix;
for ix = 1:Ns - 2
    Qm = ones(M,1)*Q(ix,:);
    rF = rF.*Qm.^-srMatrix(:,:,ix);
    rR = rR.*Qm.^sfMatrix(:,:,ix);
end
tF = ks(:,1);
tR = ks(:,2);
for ix = 1:N
    tF = tF.*rF(:,ix);
    tR = tR.*rR(:,ix);
end
r0 = [tF,tR];
r = tF - tR;
% return the equations based on P C Q kr kf
fp(1:N) = sym('0');
tp = RT*r*ones(1,N).*pMatrix;
for iy = 1:M
    fp = fp + tp(iy,:);
end
fc(1:N) = sym('0');
tc = r*ones(1,N).*cMatrix;
for iy = 1:M
    fc = fc + tc(iy,:);
end
fq(Ns - 2,1:N) = sym('0');
for ix = 1:Ns - 2
    tq = r*ones(1,N).*sMatrix(:,:,ix);
    for iy = 1:M
        fq(ix,:) = fq(ix,:) + tq(iy,:);
    end
end
% return the equations based on rate of every reaction
fpr = RT*sum(rs*ones(1,N).*pMatrix,1);
fcr = sum(rs*ones(1,N).*cMatrix,1);
for ix = 1:Ns - 2
    fqr(ix,:) = sum(rs*ones(1,N).*sMatrix(:,:,ix),1);
    Qsum(ix) = sum(Q(ix,fqr(ix,:) ~= 0));
end

disp([char(10) 'Try to Generate Kinetic Rate Equations in myRatefun.m for check now...']);
myPath = pwd;
myName = 'myRatefun';
fid = fopen([myPath '/' myName '.m'],'w');
fwrite(fid,['% The equations based on rate of every reaction :' char(10)]);
disp([ char(10) 'The equations based on rate of every reaction :']);
mywritefun(fid,FP,fpr);
mywritefun(fid,FC,fcr);
mywritefun(fid,FQ,fqr);
fwrite(fid,['% The rate equations of every reaction :' char(10)]);
disp([char(10) 'The rate equations of every reaction :' ]);
mywritefun(fid,rs,r);
fwrite(fid,['% The equations based on P C Q kr kf :' char(10)]);
disp([char(10) 'The equations based on P C Q kr kf :' ]);
mywritefun(fid,FP,fp);
mywritefun(fid,FC,fc);
mywritefun(fid,FQ,fq);
fclose(fid);

function myCreatfun(rF,rR,dy)
myPath = pwd;
myName = 'myfun';
fid = fopen([myPath '/' myName '.m'],'w');
rF = mydealstr(rF);
rR = mydealstr(rR);
dy = mydealstr(dy);
fwrite(fid,['function [dy,rF,rR] = odefun(t,y,kf,kr,RT)' char(10)]);
% fwrite(fid,['global ' globalvars ';' char(10)]);
fwrite(fid,['rF = ...' char(10) rF ';' char(10) char(10)]);
fwrite(fid,['rR = ...' char(10) rR ';' char(10) char(10)]);
fwrite(fid,['r = rF - rR;' char(10) char(10)]);
fwrite(fid,['dy = ...' char(10) dy ';' ]);
fclose(fid);
function s = mydealstr(s)
s = char(s);
s([1:8,end-1:end])=[];
% s = strrep(s,' ','');
s = strrep(s,',',[';...' char(10)]);

function mywritefun(fid,F,f)
[m,n] = size(F);
for ix = 1:m
    for iy = 1:n
        if f(ix,iy) ~= 0 
            fwrite(fid,[char(F(ix,iy)) ' = ' char(f(ix,iy)) char(10)]);
            disp([char(F(ix,iy)) ' = ' char(f(ix,iy))]);
        end
    end
end
function G = mysubs(F,X,Y)
if ~isa(F,'sym'), F = sym(F); end
if builtin('numel',F) ~= 1,  F = normalizesym(F);  end

if isempty(Y)
    G = F;
else
    % convert X,Y to all syms or all numerics, and wrap in cell array if needed
    [X2,symX] = normalize(X); %#ok
    [Y2,symY] = normalize(Y); %#ok
    
    % the evaluation in MATLAB didn't work so send all data to MuPAD for subs
    G = mupadmex('symobj::fullsubs',char(F),X2,Y2);
    if isa(F,'symfun')
        G = symfun(G,argnames(F));
    end
end

% given expression x to subs for, find string form for x in order to
% be used by anon function
function c = getchar(x)
if isa(x,'sym')
    c = char(x);
elseif ischar(x)
    c = x;
else
    c = '?'; % need any symbol that is not a variable name
end

% convert A to a MuPAD list
function s = tolist(A)
s = cellfun(@(x)[getchar(x) ','],A,'UniformOutput',false);
s = [s{:}];
s = ['[' s(1:end-1) ']'];
% convert input X to cell array of sym objects
function [X2,X] = normalize(X)
if iscell(X)
    X = cellfun(@(x)sym(x),X,'UniformOutput',false);
elseif ischar(X) || isnumeric(X)
    X = {sym(X)};
elseif isa(X,'sym')
    X = {X};
else
    error(message('symbolic:subs:InvalidXClass'));
end
% we need to keep X alive so that the reference is not collected
X2 = tolist(X); 

function globallist = GetVariables(Parameters,Pline,Variables)
globallist = 'Q0 T Ex npar';
global Q0 T Ex npar
globallist0 = globallist;
for ip = 1:length(Pline)
    varlist = regexp(Parameters{ip},';;','split');
    for ivar = 1:length(varlist)
        if ~isempty(strrep(varlist{ivar},' ' ,''))
            try
                globalvar = regexp(varlist{ivar},'=','split');
                if isempty(strfind(globalvar{1},'('))
                    globalvar{1} = strrep(globalvar{1},' ','');
                    vars = regexp(regexprep(globalvar{1},'[[,]]',' '),' ','split');
                    for ind = 1 : length(vars)
                        if (mystrMatch(strcat(Variables,'_FROZ'),vars{ind}) ...
                                || mystrMatch(strcat(Variables,'_INIT'),vars{ind}) ...
                                || mystrMatch(strcat(Variables,'_EQUI'),vars{ind}));
                            globallist0 = [globallist ' ' vars{ind}];
                            warning off;
                            try
                                eval(['global ' vars{ind}]);
                            catch
                                disp(['Illegal Variable: ' vars{ind}]);
                                globallist0 = globallist;
                            end
                            warning on;
                        end
                    end
                end
                eval([varlist{ivar} ';']);
                disp([varlist{ivar} ';'])
                globallist = globallist0;
            catch err
                id = err.identifier;
                fprintf('%s: %s at line %d\n',id,varlist{ivar},Pline(ip));
            end
        end

    end
end

function [globalvars,yChan,yEqui,yInit,lmax,yp,mysym] = Initialization(osym0,globallist,fpr,fcr,fqr,r0)
Nsyms = length(osym0);
if ~isempty(globallist)
    eval(['global ' globallist]);
end
globalvars = '';
warnstr = warning('off', 'Control:parameterNotSymmetric');
for i = 1:Nsyms ;
    try
        yChan(i) = false;
        eval([osym0{i} '_FROZ;']);
        globalvars = [globalvars ' ' osym0{i}];
        eval(['global ' osym0{i}]);
        eval([osym0{i} ' = ' osym0{i} '_FROZ;']);
    catch
        yChan(i) = true;
    end
    try
        eval([ 'yEqui(i) = ' osym0{i} '_EQUI;']);
    catch
        yEqui(i) = 0;
    end   
    try
        eval([ 'yInit(i) = ' osym0{i} '_INIT;']);
    catch
        yInit(i) = 0;
    end     
end
warning(warnstr);
lmax = 0;
osym0 = osym0(yChan);
for ix = 1:length(osym0)
    lmax = max(lmax,length(osym0{ix}));
    nsym(ix) = sym(['y(' num2str(ix) ')']);
    osym(ix) = sym(osym0{ix});
end
rF = subs(r0(:,1),osym,nsym);
rR = subs(r0(:,2),osym,nsym);
mysym = [nsym;osym];
disp([char(10) 'Try to Generate Kinetic Rate Equations in odefun.m for ODE solver now...']);
dy = [fpr;fcr;fqr].';
dy = dy(:);
yp = dy ~= 0;
dy = dy(yp);
dy = dy(yChan);
myCreatfun(subs(rF).',subs(rR).',subs(dy).');


function [kf,kr] = RateConstCalc(Ea,G0)
global keV kBT_h
Keq = exp(-G0*keV);
kf = exp(-Ea*keV)*kBT_h;
kr = kf./Keq;

function solix = myfsolve(symfuns,ys,yinit,myDigit)
ystr = [];
for i = 1:length(ys);
    ystr = strcat(ystr,[ys{i} ' = ' num2str(yinit(i)) ', ']);
end
ystr(end) = [];
solix = evalin(symengine,['DIGITS := ' num2str(myDigit) ': numeric::fsolve({',symfuns, '},[' ystr '])']);

function ysol = mygetsol(solix,ysym)
sols = strrep(strrep(char(solix),'matrix([',''),']','');
eval([strrep(strrep(sols(2:end - 1),' == ','_new = sym('''),',',''');') ''');']);
ysol = eval(['['  [strrep(ysym,',','_new, ') '_new'] ']']);

function [te,y,dy,Rnet,Rfr] = myodes(tspan,yInit,options,kf,kr,RT)
Nb = ceil(log10(tspan(2)));
Na = 1;
NT = (Nb - Na + 1);
[t,x]=ode15s(@odefun,[0 logspace(Na,Nb,NT)],yInit,options,kf,kr,RT);
te = t(end);
y = x(end,:);
[dy,rF,rR] = odefun([],y,kf,kr,RT);
Rfr = [rF rR];
Rnet = rF - rR;

function [ysol,solveStatus] = tryfsolve(symfuns,yInit,ysym,ytry,kf,kr,RT,Y0)
[ystr,ysort] = sort(regexp(ysym,',','split'));
tspan=[0 1e4];
options=odeset('AbsTol', 1e-50, 'RelTol',100*eps);
Maxtry1 = 1000;
Maxtry2 = 20;
Maxtry3 = 20;
tscale = 100;
kscale = 0.001;
N_ode15s1 = 1;
N_ode15s2 = 8;
ND0 = 150;
NC = 20;
digits(500);
%% try and solve in numeric
isFail = 1;
tryTimes1 = 0;
Yi = 0;
Ninit = size(Y0,1);
[~,ytry,~,~,~] = myodes([0 10],yInit,options,kf,kr,RT);
while isFail && tryTimes1 < Maxtry1
    % initial starting points at y0 for default
    if tryTimes1 == 0
        solix = myfsolve(symfuns,ystr,ytry,1000);
    else
        solix = myfsolve(symfuns,ystr,ytry,1000);
    end
    if ~isempty(strfind(char(solix),'== -'))
        disp([char(10) 'Try numeric::fsolve results a negative solution, try fine control now...']);
        ytry = double(mygetsol(solix,ysym));
        ytry = ytry(ysort).';
        yrange = 1000;
        tryTimes3 = 0;
        isFail = 1;
        while isFail && tryTimes3 <= Maxtry3
            yrange = yrange * kscale;
            yn = ytry;
            yn( yn < 0 ) = yrange;
            solix = myfsolve(symfuns,ystr,yn,100);
            isFail = strcmp(char(solix),'FAIL') || ~isempty(strfind(char(solix),'== -'));
            tryTimes3 = tryTimes3 + 1;
        end
    end
    isFail = strcmp(char(solix),'FAIL') || ~isempty(strfind(char(solix),'== -'));
    
    if isFail
        disp([char(10) 'Try numeric::fsolve failed ...'])
        if  tryTimes1 < N_ode15s1
            disp([char(10) 'Try numeric::fsolve at state from ODE15S solver in time span of [0,' num2str(tspan(2)) '] now...']);
            % get the starting points from the solutuion by ode15s
            % increase ending time: tspan(2) = tspan(2) * tscale
            [~,ytry,~,~,~] = myodes(tspan,yInit,options,kf,kr,RT);
            tspan(2) = tspan(2) * tscale;
            yode = ytry;
        elseif Yi < Ninit
            Yi = Yi + 1;
            disp([char(10) 'Try numeric::fsolve at extreme conditions now...']);
            ytry = 0.9999*Y0(Yi,:);
        elseif tryTimes1 < N_ode15s1 + Ninit
            disp([char(10) 'Try numeric::fsolve at state from numeric::solve at diffrent digits now...']);
            % numeric::solve % try solve at diffrent digits
            isFail2 = 1;
            ND = ND0;
            tryTimes2 = 0;
            while isFail2 && tryTimes2 < Maxtry2
                digits(ND);
                solix = evalin(symengine,['numeric::solve({',symfuns, '},[' ysym '])']);
                isFail2 = ~isempty(strfind(char(solix),'{}')) || length(solix) ~= 1;
                tryTimes2 = tryTimes2 + 1;
                ND = ND + NC;
            end
            solix = solix(1);
            digits(ND0);
            if ~isempty(strfind(char(solix),'{}'))
                disp([char(10) 'Try numeric::solve failed, give a state by random ...']);
                ytry = rand(1,length(yInit));
            else
                disp([char(10) 'numeric::solve gives a state at digits: ' num2str(ND-NC) '...']);
                ytry = double(mygetsol(solix,ysym));
                ytry = ytry(ysort).';
            end
        elseif tryTimes1 < N_ode15s1 + N_ode15s2 + Ninit
            disp([char(10) 'Try numeric::fsolve at state from ODE15S solver in time span of [0,' num2str(tspan(2)) ']...']);
            % get the starting points from the solutuion by ode15s
            % increase ending time: tspan(2) = tspan(2) * tscale
            [~,ytry,~,~,~] = myodes(tspan,yInit,options,kf,kr,RT);
            yode = ytry;
            tspan(2) = tspan(2) * tscale;
        else
            disp([char(10) 'Try numeric::fsolve at states by random now...']);
            % random create a starting points
            ytry = rand(1,length(yInit));
        end
    end
    tryTimes1 = tryTimes1 + 1;
end
if isFail
    disp('Could not extract individual solutions by numeric::fsolve');
    disp(['Extract individual solutions by numeric::ode15s at tspan ' num2str(tspan(end))] );
    ysol = yode;
    solveStatus = 4;
else
    disp('Extract individual solutions by numeric::fsolve');
    ysol = mygetsol(solix,ysym);
    ysol = ysol(ysort).';
    solveStatus = 3;
end

function [G0,Ea] = initGE(E_O)
E_TdS = [0.703790904 0.746670653 0.686495916];
ETdS_NO = E_TdS(1);
ETdS_NO2 = E_TdS(2);
ETdS_O2 = E_TdS(3);
%dG0 = -1.18599975 + ETdS_NO2 - ETdS_NO - ETdS_O2/2; % NO + 1/2 O2 <-> NO2 dG
E_NO = 0.0938*E_O - 0.7335;
ETS_ONO= 0.0932*E_O + 0.0559;
E_ONO = 0.3447*E_O - 1.0223;
E1_NO2 = 0.5615*E_O + 0.5698;
E_O2 = 0.6799*E_O - 0.0375;
E_N = 0.1905*E_O - 0.7688;
ETS_N = -0.1871*E_O + 0.5824;
EFS_NO2 = 0.5144*E_O + 0.597;
E2_NO2 = 0.1004*E_O + 0.8032;
G0(1) = E_NO + ETdS_NO;           % NO + #1 <-> ON#1   
G0(2) = E_ONO;                    % ON#1 + O#2 <-> ONO#2 + #1
G0(3) = E1_NO2 - ETdS_NO2;        %ONO#2 <-> NO2 + #2
G0(4) = E_O2 + ETdS_O2;           %O2 + #2 <-> O2#2
G0(5) = E_N;                   %O2#2 + ON#1 <-> N#2 + #1
G0(6) = EFS_NO2;                 %N#2 + #1 <-> NO2#1 + O#2  
G0(7) = E2_NO2 - ETdS_NO2;        % NO2#1 <-> NO2 + #1
Ea(1) = max(1/3*ETdS_NO,G0(1));   %NO + #1 <-> ON#1  
Ea(2) = ETS_ONO;                  %ON#1 + O#2 <-> ONO#2 + #1    
Ea(3) = max(0,G0(3) + 1/3*ETdS_NO2);   %ONO#2 <-> NO2 + #2   
Ea(4) = max(1/3*ETdS_O2,G0(4));        %O2 + #2 <-> O2#2
Ea(5) = max(0,G0(5));                  %O2#2 + ON#1 <-> N#2 + #1
Ea(6) = ETS_N;                      %N#2 + #1 <-> NO2#1 + O#2  
Ea(7) = max(0,G0(7) + 1/3*ETdS_NO2);   %NO2#1 <-> NO2 + #1 