reset=`tput sgr0`
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`

LOG_INFO()
{
    echo "${green}[i] $1${reset}"
}

LOG_WARN()
{    
    echo "${yellow}[w] $1${reset}"
}

LOG_ERR()
{ 
    echo "${red}[e] $1${reset}" 
}


if [ $# -ne 1 ]; then
    LOG_ERR "Usage: $0 <output_dir>"
    exit 1
fi


i=0
success=0
failed=0
for file in *.proto; do 
    i=$((i+1))
    echo "Compiling $file"
    #./protoc-3.1.0 --python_out=pyi_out:$1 $file
    protoc --python_out=pyi_out:$1 $file
    if [ $? -eq 0 ]; then
        success=$((success+1))
        LOG_INFO "$file compiled successfully"
    else
        failed=$((failed+1))
        LOG_ERR "$file failed to compile"
    fi
done

LOG_INFO "Total: $i, Success: $success, Failed: $failed"
