// Blueprint Implementable
// Program 022

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program022.generated.h"

UCLASS()
class AProgram022 : public AActor
{
    GENERATED_BODY()

public:
    AProgram022();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
