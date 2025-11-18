#!/usr/bin/perl
use strict;
use warnings;

print "=== Perl Regex Matcher ===\n";
print "Enter text: ";
my $text = <STDIN>;
chomp($text);

print "Enter pattern: ";
my $pattern = <STDIN>;
chomp($pattern);

if ($text =~ /$pattern/) {
    print "Match found!\n";
    print "Matched text: $&\n" if defined $&;

    if (@{^CAPTURE}) {
        print "Captured groups:\n";
        for (my $i = 0; $i < @{^CAPTURE}; $i++) {
            print "  Group $i: " . ${^CAPTURE}[$i] . "\n";
        }
    }
} else {
    print "No match found\n";
}
