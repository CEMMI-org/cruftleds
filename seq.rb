file = File.new("patterns.txt","r");
lines = []
i=0;
while (line = file.gets)
   lines[i] = line;
   i = i+1;
end

lines.each{ |x| system("python "+x);};
