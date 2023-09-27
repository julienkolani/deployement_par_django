{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e89b1535-a98e-4c1f-87d0-76bb4c31ca86",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "\n",
    "# Définir les chemins et les informations spécifiques au projet\n",
    "venv_path = '/home/app/my_app_venv/bin/activate'\n",
    "manage_py_path = '/home/app/test_app/manage.py'\n",
    "unitd_control_socket = '/var/run/control.unit.sock'\n",
    "unit_out_log = '/home/app/out.log'\n",
    "unit_config_socket = '/run/control.unit.sock'\n",
    "unit_config_url = 'http://localhost/config'\n",
    "run_sh_output = 'run.sh'\n",
    "\n",
    "# Générer le contenu du fichier run.sh\n",
    "run_sh_content = f'''#!/bin/sh\n",
    "\n",
    "# Activer l'environnement virtuel\n",
    ". {venv_path}\n",
    "\n",
    "# Collecter les fichiers statiques\n",
    "{manage_py_path} collectstatic --noinput\n",
    "\n",
    "# Désactiver l'environnement virtuel\n",
    "deactivate\n",
    "\n",
    "# Exécuter unitd en arrière-plan et rediriger la sortie vers {unit_out_log}\n",
    "unitd --no-daemon --control unix:{unitd_control_socket} > {unit_out_log} 2>&1 &\n",
    "\n",
    "# Exécuter curl pour configurer Unit\n",
    "curl -X PUT --data-binary @{unit_config_socket} --unix-socket {unit_config_url}\n",
    "\n",
    "tail -f /dev/null\n",
    "'''\n",
    "\n",
    "# Écrire le contenu généré dans le fichier run.sh\n",
    "with open(run_sh_output, 'w') as file:\n",
    "    file.write(run_sh_content)\n",
    "\n",
    "print(f'Le fichier {run_sh_output} a été généré avec succès.')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
