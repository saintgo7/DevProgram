// Niagara
// Program 072

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program072.generated.h"

UCLASS()
class AProgram072 : public AActor
{
    GENERATED_BODY()

public:
    AProgram072();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
