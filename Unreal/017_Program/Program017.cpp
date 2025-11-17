// UActorComponent

#include "Program017.h"

AProgram017::AProgram017()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram017::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== UActorComponent ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating uactorcomponent."));

    // Implement the program logic here...
}

void AProgram017::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
