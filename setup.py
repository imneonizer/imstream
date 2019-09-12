from distutils.core import setup
setup(
  name = 'imstream',         # How you named your package folder (MyLib)
  packages = ['imstream'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The most exciting and powerful "video /  webcam" streamer for python it is built on top of OpenCV and threading module. It provides ultra fast *FPS 400+ when streamed.',   # Give a short description about your library
  author = 'Nitin Rai',                   # Type in your name
  author_email = 'mneonizer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/imneonizer/imstream',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/imneonizer/imstream/archive/v0.1.0.tar.gz',    # I explain this later on
  keywords = ['Ultra Fast FPS', 'Webcam Streaming', 'Multi threading'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
