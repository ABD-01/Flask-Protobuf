if [ $# -ne 1 ]; then
    echo "Usage: $0 <output_dir>"
    exit 1
fi


i=0
for file in *.proto; do 
    echo "$file" 
    i=$((i+1))
    echo "Compiling $file"
    #./protoc-3.1.0 --python_out=pyi_out:$1 $file
    protoc --python_out=pyi_out:$1 $file
done

echo "Num Files: $i"
