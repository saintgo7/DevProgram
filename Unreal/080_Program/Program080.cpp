// Ambient Sound

#include "Program080.h"

AProgram080::AProgram080()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram080::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Ambient Sound ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating ambient sound."));

    // Implement the program logic here...
}

void AProgram080::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
