// Death

#include "Program045.h"

AProgram045::AProgram045()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram045::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Death ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating death."));

    // Implement the program logic here...
}

void AProgram045::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
