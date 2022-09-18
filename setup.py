from setuptools import setup, find_packages

# http://www.diveintopython3.net/packaging.html
# https://pypi.python.org/pypi?:action=list_classifiers

with open('README.md') as file:
    long_description = file.read()

setup(
    name='pynats',
    packages=find_packages(),
    package_data={'': ['config.yaml',
			'data/forex.npy',
			'data/cml.npy',
                        'lib/jidt/infodynamics.jar',
                        'lib/PhiToolbox/Phi/phi_comp.m',
                        'lib/PhiToolbox/Phi/phi_star_Gauss.m',
                        'lib/PhiToolbox/Phi/phi_G_Gauss.m',
                        'lib/PhiToolbox/Phi/phi_G_Gauss_AL.m',
                        'lib/PhiToolbox/Phi/phi_G_Gauss_LBFGS.m',
                        'lib/PhiToolbox/Phi/phi_comp_probs.m',
                        'lib/PhiToolbox/Phi/phi_Gauss.m',
                        'lib/PhiToolbox/utility/I_s_I_s_d.m',
                        'lib/PhiToolbox/utility/data_to_probs.m',
                        'lib/PhiToolbox/utility/Gauss/Cov_comp.m',
                        'lib/PhiToolbox/utility/Gauss/Cov_cond.m',
                        'lib/PhiToolbox/utility/Gauss/H_gauss.m',
                        'lib/PhiToolbox/utility/Gauss/logdet.m']},
    include_package_data=True,
    version='0.2.2',
    description='Network analysis for time series',
    author='Oliver M. Cliff',
    author_email='oliver.m.cliff@gmail.com',
    url='https://github.com/olivercliff/pynats',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    install_requires=['pytest',
                        'scikit-learn>=0.24.1',
                        'scipy==1.5.4',
                        'numpy==1.19.5', 
                        'statsmodels>=0.12.0',
                        'pyyaml>=5.3.1',
                        'tqdm>=4.50.2',
                        'nitime==0.9',
                        'hyppo==0.2.1',
                        'pyEDM>=1.0.3.2',
                        'jpype1>=1.2.0',
                        'sktime==0.4.3',
                        'dill>=0.3.2',
                        'spectral-connectivity>=0.2.4.dev0',
                        'umap-learn>=0.4.6',
                        'torch>=1.7.0',
                        'cdt==0.5.23',
                        'oct2py==5.2.0',
                        'dtw-python==1.1.10',
                        'tslearn==0.5.1',
                        'mne==0.23.0',
                        'seaborn==0.11.0']
)
