file = File.new("patterns.txt","r");
lines = []
i=0;
while (line = file.gets)
   lines[i] = line;
   i = i+1;
end

while (1)
  r = (lines.length()*rand).floor()
  print(r);
  print("\n");
  system("python2.7 "+lines[r])
end
