// Character

#include "Program004.h"

AProgram004::AProgram004()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram004::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Character ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating character."));

    // Implement the program logic here...
}

void AProgram004::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
