// Death
// Program 045

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program045.generated.h"

UCLASS()
class AProgram045 : public AActor
{
    GENERATED_BODY()

public:
    AProgram045();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
