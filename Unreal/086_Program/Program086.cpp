// Raycast

#include "Program086.h"

AProgram086::AProgram086()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram086::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Raycast ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating raycast."));

    // Implement the program logic here...
}

void AProgram086::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
