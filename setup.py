from setuptools import setup,find_packages

HYPEN_E_DOT="-e ."

def get_requirements(file_path):
    requirements=[]
    with open(file_path,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name="heart_disease_prediction",
    author="Khizer Dawood",
    author_email="khizerkhan81009@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)