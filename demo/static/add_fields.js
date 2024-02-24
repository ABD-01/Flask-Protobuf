function generateRepeatedFields(n, template, placeholder='{index}') {
    let listItems = [];
    for (let i = 0; i <= n; i++) {
      listItems.push(template.replaceAll(placeholder, i));
    }
    return listItems.join(' ');
}

function get_additional_fields(subtype, numEntries){
    
    if (subtype == 0) {
        return ``;
    }

    
    if (subtype == 1) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 2) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 3) {
        return ``;
    }

    // Handle repetition Here
    if (subtype == 4) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <ul class="list-group list-unstyled" id="Field-1">`
                +
                generateRepeatedFields(numEntries, `<li><label for="Field-1-{index}">Field-1-{index}</label> <table class="table table-bordered" id="Field-1-{index}"> <tr> <th><label for="Field-1-{index}-Nested-Field-0">Nested-Field-0</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-0" name="Field-1-{index}-Nested-Field-0" type="text" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-1">Nested-Field-1</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-1" name="Field-1-{index}-Nested-Field-1" type="text" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-2">Nested-Field-2</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-2" name="Field-1-{index}-Nested-Field-2" type="text" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-3">Nested-Field-3</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-3" name="Field-1-{index}-Nested-Field-3" type="text" value=""></td> </tr> </table> </li>`)
                + 
                `</ul>
                
            </div>
        </div>`;
    }

    
    if (subtype == 5) {
        return ``;
    }

    
    if (subtype == 6) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 7) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 8) {
        return ``;
    }

    
    if (subtype == 9) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 10) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 11) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-0" name="Field-0"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option><option value="2">Enum-Options-2</option><option value="3">Enum-Options-3</option></select>
                
            </div>
        </div>`;
    }

    // Handle repetition Here
    if (subtype == 12) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <ul class="list-group list-unstyled" id="Field-1">`
                +
                generateRepeatedFields(numEntries, `<li><label for="Field-1-{index}">Field-1-{index}</label> <table class="table table-bordered" id="Field-1-{index}"> <tr> <th><label for="Field-1-{index}-Nested-Field-0">Nested-Field-0</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-0" name="Field-1-{index}-Nested-Field-0" type="number" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-1">Nested-Field-1</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-1" name="Field-1-{index}-Nested-Field-1" type="text" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-2">Nested-Field-2</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-2" name="Field-1-{index}-Nested-Field-2" type="number" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-3">Nested-Field-3</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-3" name="Field-1-{index}-Nested-Field-3" type="checkbox" value="y"></td> </tr> </table> </li>`)
                +
                `</ul>
                
            </div>
        </div>`;
    }

    
    if (subtype == 13) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-2" class="col-auto col-form-label"><label for="Field-2">Field-2</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-2" name="Field-2" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-3" class="col-auto col-form-label"><label for="Field-3">Field-3</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-3" name="Field-3" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-4" class="col-auto col-form-label"><label for="Field-4">Field-4</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-4" name="Field-4" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-5" class="col-auto col-form-label"><label for="Field-5">Field-5</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-5" name="Field-5" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-6" class="col-auto col-form-label"><label for="Field-6">Field-6</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-6" name="Field-6" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-7" class="col-auto col-form-label"><label for="Field-7">Field-7</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-7" name="Field-7" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-8" class="col-auto col-form-label"><label for="Field-8">Field-8</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-8" name="Field-8" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 14) {
        return ``;
    }

    
    if (subtype == 15) {
        return ``;
    }

    
    if (subtype == 16) {
        return ``;
    }

    
    if (subtype == 17) {
        return ``;
    }

    
    if (subtype == 18) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-0" name="Field-0"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 19) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-2" class="col-auto col-form-label"><label for="Field-2">Field-2</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-2" name="Field-2" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-3" class="col-auto col-form-label"><label for="Field-3">Field-3</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-3" name="Field-3" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-4" class="col-auto col-form-label"><label for="Field-4">Field-4</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-4" name="Field-4"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option><option value="2">Enum-Options-2</option><option value="3">Enum-Options-3</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 20) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-2" class="col-auto col-form-label"><label for="Field-2">Field-2</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-2" name="Field-2" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-3" class="col-auto col-form-label"><label for="Field-3">Field-3</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-3" name="Field-3" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-4" class="col-auto col-form-label"><label for="Field-4">Field-4</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-4" name="Field-4" type="text" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 21) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 22) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-2" class="col-auto col-form-label"><label for="Field-2">Field-2</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-2" name="Field-2"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option><option value="2">Enum-Options-2</option><option value="3">Enum-Options-3</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 23) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-0" name="Field-0"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option><option value="2">Enum-Options-2</option><option value="3">Enum-Options-3</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 24) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 25) {
        return ``;
    }

    
    if (subtype == 26) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>`;
    }

    // Handle repetition Here
    if (subtype == 27) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <ul class="list-group list-unstyled" id="Field-0">`
                +
                generateRepeatedFields(numEntries, `<li><label for="Field-0-{index}">Field-0-{index}</label> <table class="table table-bordered" id="Field-0-{index}"> <tr> <th><label for="Field-0-{index}-Nested-Field-0">Nested-Field-0</label></th> <td><input class="form-control form-control-sm" id="Field-0-{index}-Nested-Field-0" name="Field-0-{index}-Nested-Field-0" type="text" value=""></td> </tr> <tr> <th><label for="Field-0-{index}-Nested-Field-1">Nested-Field-1</label></th> <td><input class="form-control form-control-sm" id="Field-0-{index}-Nested-Field-1" name="Field-0-{index}-Nested-Field-1" type="text" value=""></td> </tr> </table> </li>`)
                +
                `</ul>
                
            </div>
        </div>`;
    }

    
    if (subtype == 28) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-0" name="Field-0"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 29) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-2" class="col-auto col-form-label"><label for="Field-2">Field-2</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-2" name="Field-2" type="text" value="">
                
            </div>
        </div>`;
    }

    
    if (subtype == 30) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="text" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-1" name="Field-1" type="text" value="">
                
            </div>
        </div>`;
    }

    // Handle repetition Here
    if (subtype == 31) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <input class="form-control form-control-sm" id="Field-0" name="Field-0" type="number" value="">
                
            </div>
        </div>
    

    
        <div class="form-group row gap-0">
            <label for="Field-1" class="col-auto col-form-label"><label for="Field-1">Field-1</label></label>
            <div class="col-auto">
                <ul class="list-group list-unstyled" id="Field-1">`
                +
                generateRepeatedFields(
                    numEntries,
                    `<li><label for="Field-1-{index}">Field-1-{index}</label> <table class="table table-bordered" id="Field-1-{index}"> <tr> <th><label for="Field-1-{index}-Nested-Field-0">Nested-Field-0</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-0" name="Field-1-{index}-Nested-Field-0" type="number" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-1">Nested-Field-1</label></th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-1" name="Field-1-{index}-Nested-Field-1" type="number" value=""></td> </tr> <tr> <th><label for="Field-1-{index}-Nested-Field-2">Nested-Field-2</label></th> <td> <ul class="list-group list-unstyled" id="Field-1-{index}-Nested-Field-2">` 
                    +
                    generateRepeatedFields(numEntries, `<li><label for="Field-1-{index}-Nested-Field-2-{nestedIndex}">Nested-Field-2-{nestedIndex}</label> <table class="table table-bordered" id="Field-1-{index}-Nested-Field-2-{nestedIndex}"> <tr> <th><label for="Field-1-{index}-Nested-Field-2-{nestedIndex}-Nested-Nested-Field-0">Nested-Nested-Field-0</label> </th> <td><input class="form-control form-control-sm" id="Field-1-{index}-Nested-Field-2-{nestedIndex}-Nested-Nested-Field-0" name="Field-1-{index}-Nested-Field-2-{nestedIndex}-Nested-Nested-Field-0" type="number" value=""> </td> </tr> </table> </li>`, '{nestedIndex}')
                    +
                    `</ul> </td> </tr> </table> </li>`
                )
                +
                `</ul>
                
            </div>
        </div>`;
    }

    
    if (subtype == 32) {
        return `<div class="form-group row gap-0">
            <label for="Field-0" class="col-auto col-form-label"><label for="Field-0">Field-0</label></label>
            <div class="col-auto">
                <select class="form-select form-select-sm" id="Field-0" name="Field-0"><option value="0">Enum-Options-0</option><option value="1">Enum-Options-1</option><option value="2">Enum-Options-2</option><option value="3">Enum-Options-3</option><option value="4">Enum-Options-4</option><option value="5">Enum-Options-5</option></select>
                
            </div>
        </div>`;
    }

    
    if (subtype == 33) {
        return ``;
    }
}