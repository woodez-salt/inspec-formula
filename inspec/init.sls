dev_inspec_linux_script:
  file.managed:
    - name: /var/tmp/run_inspec_linux.sh
    - source: salt://inspec/files/run_inspec_linux.sh

collection_inspec_script:
  file.managed:
    - name: /var/tmp/get_inspec_results.py
    - source: salt://inspec/files/get_inspec_results.py


remove_src:
  file.absent:
    - name: /var/tmp/inspec-test/

git_inspec_code:
  cmd.run:
    - name: git clone https://github.com/woodez-salt/inspec-formula.git /var/tmp/inspec-test 


run_test:
  cmd.run:
    - name: bash /var/tmp/run_inspec_linux.sh

get_inspec_results:
  cmd.run:
    - name: python /var/tmp/get_inspec_results.py
 
