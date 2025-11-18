#!/usr/bin/perl
use strict;
use warnings;

print "=== Perl Calculator ===\n";
print "Enter first number: ";
my $num1 = <STDIN>;
chomp($num1);

print "Enter operator (+, -, *, /): ";
my $op = <STDIN>;
chomp($op);

print "Enter second number: ";
my $num2 = <STDIN>;
chomp($num2);

my $result;

if ($op eq '+') {
    $result = $num1 + $num2;
} elsif ($op eq '-') {
    $result = $num1 - $num2;
} elsif ($op eq '*') {
    $result = $num1 * $num2;
} elsif ($op eq '/') {
    if ($num2 != 0) {
        $result = $num1 / $num2;
    } else {
        print "Error: Division by zero\n";
        exit 1;
    }
} else {
    print "Invalid operator\n";
    exit 1;
}

print "Result: $num1 $op $num2 = $result\n";
