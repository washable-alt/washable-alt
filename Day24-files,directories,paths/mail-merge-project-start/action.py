
PLACEHOLDER = "[name]"


class Action:

    def __init__(self):
        self.name = [] 
        self.email = []
     
    def format_file(self):

        try:
            with open(f".\\Day24-files,directories,paths\\mail-merge-project-start\\Input\\Names\\invited_names.txt", 'rt') as f:
                names = f.readlines()

            with open(f".\\Day24-files,directories,paths\\mail-merge-project-start\\Input\\Letters\\starting_letter.docx") as sl:
                letter_contents = sl.read()
                for name in names:
                    stripped_name = name.strip()
                    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
                    self.output_file(stripped_name,new_letter)

        except Exception as e:
            print(e)

    def output_file(self, name ,contents):
        with open(f".\\Day24-files,directories,paths\\mail-merge-project-start\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(contents)

    

                

