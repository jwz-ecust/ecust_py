function [Reactions,Rline,Parameters,Pline] = ReadINCAR(INCAR1)
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






