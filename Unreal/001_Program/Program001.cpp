// Hello World

#include "Program001.h"

AProgram001::AProgram001()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram001::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Hello World ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating hello world."));

    // Implement the program logic here...
}

void AProgram001::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
