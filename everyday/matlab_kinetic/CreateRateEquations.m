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
