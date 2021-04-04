# install puppet-lint package
package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
