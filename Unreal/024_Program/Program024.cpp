// Blueprint Library

#include "Program024.h"

AProgram024::AProgram024()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram024::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blueprint Library ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blueprint library."));

    // Implement the program logic here...
}

void AProgram024::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
