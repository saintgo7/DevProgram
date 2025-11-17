// Blueprint Interface
// Program 025

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program025.generated.h"

UCLASS()
class AProgram025 : public AActor
{
    GENERATED_BODY()

public:
    AProgram025();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
