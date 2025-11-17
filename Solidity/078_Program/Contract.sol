// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Commit Reveal
 * @dev Program 078
 */
contract Program078 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Commit Reveal");
    }
}
