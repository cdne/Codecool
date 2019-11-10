# Export functions
def export_data(function):
    with open('exported_data.txt', 'w') as export_file:
        export_file.write(str(function))